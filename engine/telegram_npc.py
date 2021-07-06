from functools import wraps

from dataclasses import dataclass
from re import sub
from types import SimpleNamespace

from numbers import Number
from typing import Callable, List, Tuple, Dict
from telegram import parsemode

from telegram.ext import InlineQueryHandler, Dispatcher, Filters, MessageFilter
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.message import Message

from engine.types import AbstractAction, Performance, AbstractSession
from engine.var import Var, VarKey, VarSession

import telegram
import telegram.ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

ok_markup = InlineKeyboardMarkup.from_button(InlineKeyboardButton('Понятно', callback_data='ok'))

import datetime

from threading import Thread

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
    stickerset: Dict[str, str]

    # typing text for some time

    def typing(self, length, chat_id):
        self.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        time.sleep(length/self.typing_speed)


    # bind handler
    
    def BIND(self, handler_gen: Callable[[AbstractSession, Callable], None]):
        
        def _bind(session: AbstractSession, resume: Callable):
            session.handler = handler_gen(session, resume)
            self.dispatcher.add_handler(session.handler)

        def _remove(session: AbstractSession):
            self.dispatcher.remove_handler(session.handler)

        return Performance.BIND(_bind, _remove)

    # NPC Actions

    @dataclass
    class Say(AbstractAction, method):

        PREPARE_LENGTH = 6

        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(self.PREPARE_LENGTH+len(self.text), session.chat_id)
            self.npc.bot.send_message(chat_id=session.chat_id, text=self.text)
            return Performance.MOVE_ON()

        @property
        def reading_length(self):
            return self.PREPARE_LENGTH + len(self.text)


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
            options_markup = InlineKeyboardMarkup.from_row([InlineKeyboardButton(text=o[0], callback_data=o[1]) for o in self.options])
            
            self.npc.typing(len(self.text), session.chat_id)
            self.npc.bot.send_message(chat_id=session.chat_id,
                                    text=self.text,
                                    reply_markup=options_markup)

            def options_handler(session: VarSession, resume: Callable):
                def cb(update: telegram.Update, context):
                    update.callback_query.answer()
                    update.callback_query.message.edit_reply_markup()
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

    @dataclass
    class Sticker(AbstractAction, method):

        name: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.bot.send_sticker(session.chat_id,
                                      self.npc.stickerset[self.name])
            return Performance.MOVE_ON()

    @dataclass
    class Timer(AbstractAction, method):

        minutes: int

        def generate_remaining_time(self, timer_end):
            current_time = datetime.datetime.now()

            ms = lambda s: f"{s//60}:{'0'*(2-len(str(s%60)))}{s%60}"
            if current_time > timer_end:
                return None
            else:
                return ms((timer_end-current_time).seconds)

        def perform(self, session: AbstractSession) -> Performance:
            minutes_word = "минута" if self.minutes == 1 else "минут" if self.minutes >= 5 else "минуты"
            self.npc.bot.send_message(session.chat_id,
                                      text=f"У вас есть <b>{self.minutes} {minutes_word}</b> на выполнение этого задания. Если вы закончите раньше, напишите <b>Готово</b> в чат",
                                      parse_mode = ParseMode.HTML)

            session.timer_end = datetime.datetime.now() + datetime.timedelta(0, self.minutes*60)
            session.timer_active = True
            
            session.timer_message = self.npc.bot.send_message(session.chat_id,
                                      text=f"У вас осталось: <b>{self.generate_remaining_time(session.timer_end)}</b>",
                                      parse_mode = ParseMode.HTML)            

            def _bind(session: AbstractSession, resume: Callable):
                def timer_loop():
                    while session.timer_active:
                        time.sleep(3)
                        remaining_time = self.generate_remaining_time(session.timer_end)
                        if remaining_time is None:
                            session.timer_active = False
                            session.timer_message.edit_text(f"Время закончилось!",
                                                            parse_mode = ParseMode.HTML)
                            return resume()
                        else:
                            session.timer_message.edit_text(f"У вас осталось: <b>{remaining_time}</b>",
                                                            parse_mode = ParseMode.HTML)

                timer_thread = Thread(target=timer_loop, name="timer_loop")
                #timer_thread.start()

                def cb(update, context):
                    session.timer_active = False
                    resume()

                session.handler = MessageHandler(Filters.chat(session.chat_id) & Filters.regex("^Готово$"), cb)
                self.npc.dispatcher.add_handler(session.handler)

            def _remove(session: AbstractSession):
                self.npc.dispatcher.remove_handler(session.handler)
                

            return Performance.BIND(_bind, _remove)

    @dataclass
    class Kick(AbstractAction, method):

        character: 'NPC'

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.bot.kick_chat_member(session.chat_id, self.character.bot.id)
            return Performance.MOVE_ON()
        
            


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


@methodize
@dataclass
class Score:

    total: int
    manager: NPC

    def text_ui(self, value):
        bar = value*"#" + "."*(self.total - value)
        return f"Шкала Злободневности: <code>[{bar}]</code>"

    @dataclass
    class Instantiate(AbstractAction, method):

        def perform(self, session: AbstractSession) -> Performance:
            session.score_value = 0
            session.score_message = self.score.manager.bot.send_message(
                chat_id=session.chat_id,
                text=self.score.text_ui(0),
                parse_mode=ParseMode.HTML
            )
            session.score_message.pin()
            return Performance.MOVE_ON()

        
    @dataclass
    class Add(AbstractAction, method):

        augmentation: int

        def perform(self, session: AbstractSession) -> Performance:

            session.score_value += self.augmentation

            if self.augmentation != 0:
                session.score_message.edit_text(self.score.text_ui(session.score_value),
                                                parse_mode=ParseMode.HTML)
                time.sleep(0.2)
                session.score_message.unpin()
                time.sleep(0.2)
                session.score_message.pin()
                time.sleep(0.2)

            if self.augmentation > 0:
                self.score.manager.sticker('hype').perform(session)

            return Performance.MOVE_ON()
