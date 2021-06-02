from functools import wraps

from dataclasses import dataclass
from re import sub
from types import SimpleNamespace

from numbers import Number
from typing import Callable, List, Tuple

from telegram.ext import InlineQueryHandler, Dispatcher
from telegram.ext.callbackqueryhandler import CallbackQueryHandler

from engine.types import AbstractAction, Performance, AbstractSession
from engine.var import Var, VarKey, VarSession

import telegram
import telegram.ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

ok_markup = InlineKeyboardMarkup.from_button(InlineKeyboardButton('Понятно', callback_data='ok'))

def ok_handler(session, resume):
    def cb(update: telegram.Update, context):
        update.callback_query.answer(text="Приятно!")
        update.callback_query.message.edit_reply_markup()
        return resume()
    return CallbackQueryHandler(cb)

import time


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
        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(len(self.text), session.chat_id)
            self.npc.bot.send_message(chat_id=session.chat_id, text=self.text)
            return Performance.MOVE_ON()


    @dataclass
    class Info(AbstractAction, method):

        PREPARE_LENGTH = 20

        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(self.PREPARE_LENGTH, session.chat_id)
            self.npc.bot.send_message(chat_id=session.chat_id,
                                      text=self.text,
                                      reply_markup=ok_markup)
            
            return self.npc.BIND(ok_handler)
    

    @dataclass
    class Advice(AbstractAction, method):

        PREPARE_LENGTH = 15

        caption: str
        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(self.PREPARE_LENGTH, session.chat_id)
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
            return CallbackQueryHandler(cb)

        return self.npc.BIND(options_handler)
