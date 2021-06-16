from functools import wraps

from dataclasses import dataclass
from re import sub
from types import SimpleNamespace

from numbers import Number
from typing import Callable, List, Tuple

from telegram.ext import InlineQueryHandler, Dispatcher, Filters, MessageFilter
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.messagehandler import MessageHandler

from engine.types import AbstractAction, Performance, AbstractSession
from engine.var import Var, VarKey, VarSession

import telegram
import telegram.ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

ok_markup = InlineKeyboardMarkup.from_button(InlineKeyboardButton('Понятно', callback_data='ok'))


class SessionQueryHandler(CallbackQueryHandler):
    def __init__(self, session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = session

    def check_update(self, update):
        if update.effective_chat.id == self.session.chat_id:
            return super().check_update(update)


def ok_handler(session, resume):
    def cb(update: telegram.Update, context):
        update.callback_query.answer(text="Принято!")
        update.callback_query.message.edit_reply_markup()
        return resume()
    return SessionQueryHandler(session, cb)


@dataclass
class NewMember(MessageFilter):
    user_id: int

    def filter(self, message: telegram.Message):
        return any([u.id == self.user_id for u in message.new_chat_members])


## meta hacks

class method:
    def _enroot(self, rootname, root):
        setattr(self, rootname, root)


def add_init_method(cls, subcls):
    rootname = cls.__name__.lower()
    subname = subcls.__name__.lower()

    @wraps(subcls.__init__)
    def __method(root, *args, **kwargs):
        obj = subcls(*args, **kwargs)
        obj._enroot(rootname, root)
        return obj

    __method.__name__ = subname
    setattr(cls, subname, __method)


def methodize(cls):
    for subname in filter(lambda s: s[0].isupper(), dir(cls)):
        subcls = getattr(cls, subname)
        if isinstance(subcls, type) and issubclass(subcls, method):
            add_init_method(cls, subcls)

    return cls


import time

@methodize
@dataclass
class NPC:

    typing_speed: Number # symbols in second
    bot: telegram.Bot
    dispatcher: telegram.ext.Dispatcher

    # typing text for some time

    def typing(self, length, chat_id):
        self.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        time.sleep(length/self.typing_speed)

    # bind OK callback

    def _bind_handler(self, handler_gen: Callable[[AbstractSession, Callable], None]):
        def bind(session: AbstractSession, resume: Callable):
            session.handler = handler_gen(session, resume)
            self.dispatcher.add_handler(session.handler)
        return bind
        

    def _remove_handler(self, session: AbstractSession):
        self.dispatcher.remove_handler(session.handler)

    def BIND(self, handler_gen: Callable[[AbstractSession, Callable], None]):
        return Performance.BIND(self._bind_handler(handler_gen), self._remove_handler)

    # NPC Actions

    @dataclass
    class Say(AbstractAction, method):

        PREPARE_LENGTH = 6

        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(self.PREPARE_LENGTH+len(self.text), session.chat_id)
            self.npc.bot.send_message(chat_id=session.chat_id, text=self.text)
            return Performance.MOVE_ON()


    @dataclass
    class Info(AbstractAction, method):

        PREPARE_LENGTH = 100

        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(self.PREPARE_LENGTH, session.chat_id)
            self.npc.bot.send_message(chat_id=session.chat_id,
                                      text=self.text,
                                      reply_markup=ok_markup,
                                      parse_mode=ParseMode.MARKDOWN)
            
            return self.npc.BIND(ok_handler)
    

    @dataclass
    class Advice(AbstractAction, method):

        caption: str
        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(len(self.text)*0.5, session.chat_id)
            message_text = f"<b>[{self.caption}]</b> {self.text}"
            self.npc.bot.send_message(chat_id=session.chat_id,
                                      text=message_text,
                                      reply_markup=ok_markup,
                                      parse_mode=ParseMode.HTML)
            
            return self.npc.BIND(ok_handler)

    @dataclass
    class Ask(AbstractAction, method):

        text: str
        options: List[Tuple[str, str]]
        var: VarKey

    def perform(self, session: VarSession) -> Performance:
        options_markup = InlineKeyboardMarkup.from_row([InlineKeyboardButton(*o) for o in self.options])
        
        self.npc.typing(len(self.text), session.chat_id)
        self.npc.bot.send_message(chat_id=session.chat_id,
                                  text=self.text,
                                  reply_markup=options_markup)

        def options_handler(session: VarSession, resume: Callable):
            def cb(update: telegram.Update, context):
                update.callback_query.answer()
                session.var._set(self.var, update.callback_query.data)
                return resume()
            return SessionQueryHandler(session, cb)

        return self.npc.BIND(options_handler)

    @dataclass
    class Invite(AbstractAction, method):

        character: 'NPC'

        def perform(self, session: AbstractSession) -> Performance:

            char_name = self.character.bot.username
            char_id = self.character.bot.id

            self.npc.bot.send_message(chat_id=session.chat_id,
                                      text=f"Пожалуйста, добавьте @{char_name} в чат!")

            
            def bot_added(session: VarSession, resume: Callable):
                return MessageHandler(Filters.chat(session.chat_id) & NewMember(char_id), lambda u, c: resume())

            return self.npc.BIND(bot_added)


@methodize
@dataclass

class Ability:

    name: str
    npc: NPC

    @dataclass
    class Advice(AbstractAction, method):

        text: str

        def is_actual(self, session: AbstractSession) -> bool:
            return self.ability.name in session.abilities

        def perform(self, session: AbstractAction) -> Performance:
            adv = self.ability.npc.advice(caption=self.ability.name, text=self.text)
            return adv.perform(session)