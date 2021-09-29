import time
from functools import wraps

from dataclasses import dataclass
from re import sub
from types import SimpleNamespace

from numbers import Number
from typing import Callable, List, Tuple, Dict
from telegram import parsemode, replymarkup

from telegram.ext import InlineQueryHandler, Dispatcher, Filters, MessageFilter, CommandHandler
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.message import Message

from engine.types import AbstractAction, Performance, AbstractSession
from engine.var import Var, VarKey, VarSession

import telegram
import telegram.ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode

ok_markup = lambda bt: InlineKeyboardMarkup.from_button(InlineKeyboardButton(bt, callback_data='ok'))

import datetime

from threading import Thread

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class SessionQueryHandler(CallbackQueryHandler):
    def __init__(self, session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = session

    def check_update(self, update):
        if update.effective_chat.id == self.session.chat_id:
            return super().check_update(update)


class SessionMessageHandler(MessageHandler):
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


# meta hacks

class Method:
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
        if isinstance(subcls, type) and issubclass(subcls, Method):
            add_init_method(cls, subcls)

    return cls


@methodize
@dataclass
class NPC:
    typing_speed: Number  # symbols in second
    bot: telegram.Bot
    dispatcher: telegram.ext.Dispatcher
    stickerset: Dict[str, str]

    def send_message(self, session, *args, **kwargs):
        return self.bot.send_message(chat_id=session.chat_id, *args, **kwargs)

    # typing text for some time

    def typing(self, length, chat_id):
        self.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        time.sleep(length / self.typing_speed)

    # bind handler

    def bind(self, handler_gen: Callable[[AbstractSession, Callable], None]):

        def _bind(session: AbstractSession, resume: Callable):
            session.handler = handler_gen(session, resume)
            self.dispatcher.add_handler(session.handler)

        def _remove(session: AbstractSession):
            self.dispatcher.remove_handler(session.handler)

        return Performance.BIND(_bind, _remove)

    # NPC Actions

    @dataclass
    class Say(AbstractAction, Method):

        PREPARE_LENGTH = 6

        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(self.PREPARE_LENGTH + len(self.text), session.chat_id)
            self.npc.bot.send_message(
                chat_id=session.chat_id,
                text=self.text,
                parse_mode=ParseMode.MARKDOWN)
            return Performance.MOVE_ON()

        @property
        def reading_length(self):
            return self.PREPARE_LENGTH + len(self.text)

    @dataclass
    class Info(AbstractAction, Method):

        PREPARE_LENGTH = 100

        text: str
        button_text: str = "Понятно"

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(self.PREPARE_LENGTH, session.chat_id)

            session.ok_players = list()

            read_players = lambda: f"[ {' '.join([session.players[uid]['emoji'] for uid in session.ok_players])} ]"

            self.npc.bot.send_message(chat_id=session.chat_id,
                                      text=self.text,
                                      reply_markup=ok_markup(self.button_text + " " + read_players()),
                                      parse_mode=ParseMode.MARKDOWN)

            def _bind(session: AbstractSession, resume: Callable):

                def ok(update: telegram.Update, context):
                    uid = update.effective_user.id

                    # if not registered user
                    if uid not in session.players:
                        update.callback_query.answer()
                        return

                    if uid not in session.ok_players:
                        update.callback_query.answer(text="Принято!")
                        session.ok_players.append(uid)
                        update.callback_query.message.edit_text(
                            self.text,
                            reply_markup=ok_markup(self.button_text + " " + read_players()),
                            parse_mode=ParseMode.MARKDOWN
                        )
                    else:
                        update.callback_query.answer(text="Вы уже отметились")

                    if len(session.ok_players) == len(session.players):
                        update.callback_query.message.edit_reply_markup()
                        return resume()

                session.handler = SessionQueryHandler(session, ok)

                self.npc.dispatcher.add_handler(session.handler)

            def _remove(session: AbstractSession):
                self.npc.dispatcher.remove_handler(session.handler)

            return Performance.BIND(_bind, _remove)

    @dataclass
    class Advice(AbstractAction, Method):

        caption: str
        text: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.typing(len(self.text) * 0.5, session.chat_id)
            message_text = f"<b>[{self.caption}]</b> {self.text}"
            self.npc.bot.send_message(chat_id=session.chat_id,
                                      text=message_text,
                                      reply_markup=ok_markup,
                                      parse_mode=ParseMode.HTML)

            return self.npc.bind(ok_handler)

    @dataclass
    class Ask(AbstractAction, Method):

        text: str
        options: List[Tuple[str, str]]
        var: VarKey

        def perform(self, session: VarSession) -> Performance:

            votes = {o[1]: list() for o in self.options}

            def options_markup():
                buttons = list()

                for text, data in self.options:
                    emojis = [session.players[uid]['emoji'] for uid in votes[data]]
                    buttons.append(InlineKeyboardButton(
                        text = f"{text} [ {' '.join(emojis)} ]",
                        callback_data=data))
                                        
                return InlineKeyboardMarkup.from_column(buttons)
            
            self.npc.typing(len(self.text), session.chat_id)
            self.npc.bot.send_message(chat_id=session.chat_id,
                                      text=self.text,
                                      reply_markup=options_markup(),
                                      parse_mode=ParseMode.HTML)

            def options_handler(session: VarSession, resume: Callable):
                def cb(update: telegram.Update, context): 

                    actual_option = update.callback_query.data
                    actual_voter = update.effective_user.id

                    for option, voters in votes.items():
                        if actual_voter in voters:
                            votes[option].remove(actual_voter)

                    finished = False

                    votes[actual_option].append(actual_voter)
                    if len(votes[actual_option]) == len(session.players):
                        finished = True

                    update.callback_query.answer(text="Ваш голос принят")

                    options_dict = {o[1]: o[0] for o in self.options}

                    if finished:
                        update.callback_query.message.edit_text(
                            f"{self.text}\n\n" + f"Вы выбрали: <b>{options_dict[actual_option]}</b>",
                            parse_mode=ParseMode.HTML
                        )
                        session.var._set(self.var, actual_option)
                        return resume()
                    else:
                        update.callback_query.message.edit_reply_markup(reply_markup=options_markup())
                    
                return SessionQueryHandler(session, cb)

            return self.npc.bind(options_handler)

    @dataclass
    class Invite(AbstractAction, Method):

        character: 'NPC'

        def perform(self, session: AbstractSession) -> Performance:
            char_name = self.character.bot.username
            char_id = self.character.bot.id

            self.npc.bot.send_message(chat_id=session.chat_id,
                                      text=f"Пожалуйста, добавьте @{char_name} в чат!")

            def bot_added(session: VarSession, resume: Callable):
                return MessageHandler(Filters.chat(session.chat_id) & NewMember(char_id), lambda u, c: resume())

            return self.npc.bind(bot_added)

    @dataclass
    class Sticker(AbstractAction, Method):

        name: str

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.bot.send_sticker(session.chat_id,
                                      self.npc.stickerset[self.name])
            return Performance.MOVE_ON()

    @dataclass
    class Task(AbstractAction, Method):

        text: str
        minutes: int
        fragments: List[str]
        wrong_fragment: str
        too_big_fragment: str
        correct_fragment: str
        left_fragments: Dict[int, str]

        MAX_CHAR_DIFF = 30

        def generate_remaining_time(self, timer_end):
            current_time = datetime.datetime.now()

            ms = lambda s: f"{s // 60}:{'0' * (2 - len(str(s % 60)))}{s % 60}"
            if current_time > timer_end:
                return None
            else:
                s = (timer_end - current_time).seconds
                return (s, ms(s))

        @staticmethod
        def reduce(text):
            words = list()
            for c in ' '+text:
                if c.isalpha():
                    words[-1] += c.lower()
                else:
                    words.append('')
            if not words[-1]: words.pop(-1)
            return f" {' '.join(words)} "
                
        def perform(self, session: AbstractSession) -> Performance:

            session.timer_end = datetime.datetime.now() + datetime.timedelta(0, self.minutes * 60 + 1)
            session.timer_active = True

            session.remaining_fragments = self.fragments

            _, session.timer_text = self.generate_remaining_time(session.timer_end)

            msg_text = lambda: self.text+"\n\n"+f"У вас осталось: *{session.timer_text}*"

            session.var._data['task_positive'] = 0
            session.var._data['task_negative'] = 0

            session.timer_message = self.npc.bot.send_message(session.chat_id,
                            text=msg_text(),
                            parse_mode=ParseMode.MARKDOWN)

            def _bind(session: AbstractSession, resume: Callable):

                def finish(ahead):
                    session.var._data['task_finished_ahead'] = ahead
                    return resume()

                def timer_loop():
                    while session.timer_active:
                        s, remaining_time = self.generate_remaining_time(session.timer_end)
                        if remaining_time is None:
                            session.timer_active = False
                            session.timer_message.edit_text(self.text+"\n\n"+f"Время закончилось!",
                                                            parse_mode=ParseMode.MARKDOWN)
                            return finish(False)
                        elif remaining_time != session.timer_text and s%5 == 0:
                            session.timer_text = remaining_time
                            session.timer_message.edit_text(msg_text(),
                                                            parse_mode=ParseMode.MARKDOWN)
                        time.sleep(0.1)
                    else:
                        return finish(True)

                timer_thread = Thread(target=timer_loop, name="timer_loop")

                def check_fragment(update, context):
                    guess = update.message.text
                    for frag in session.remaining_fragments:
                        if self.reduce(frag) in self.reduce(guess):
                            if len(guess) - len(frag) > self.MAX_CHAR_DIFF:
                                self.npc.send_message(session, text=self.too_big_fragment,
                                                      parse_mode=ParseMode.MARKDOWN)
                                break
                            else:
                                session.var.task_positive += 1

                                session.remaining_fragments.remove(frag)
                                left = len(session.remaining_fragments)
                                if left in self.left_fragments.keys():
                                    reply_text = self.left_fragments[left]
                                else:
                                    reply_text = self.correct_fragment
                                self.npc.send_message(session, text=reply_text,
                                                      parse_mode=ParseMode.MARKDOWN)
                                
                                if not left:
                                    session.timer_active = False
                                break
                    else:
                        session.var.task_negative += 1
                        self.npc.send_message(session, text=self.wrong_fragment,
                                              parse_mode=ParseMode.MARKDOWN)

                session.handler = SessionMessageHandler(session, Filters.text, check_fragment)

                timer_thread.start()
                self.npc.dispatcher.add_handler(session.handler)
                
            def _remove(session: AbstractSession):
                self.npc.dispatcher.remove_handler(session.handler)

            return Performance.BIND(_bind, _remove)

    @dataclass
    class Kick(AbstractAction, Method):

        character: 'NPC'

        def perform(self, session: AbstractSession) -> Performance:
            self.npc.bot.kick_chat_member(session.chat_id, self.character.bot.id)
            return Performance.MOVE_ON()

    @dataclass
    class Acquaintance(AbstractAction, Method):

        text: str
        emojis: str

        def perform(self, session: AbstractSession) -> Performance:

            session.players = dict()

            def emoji_keyboard():
                occupied_emojis = [u['emoji'] for u in session.players.values()]
                available_emojis = filter(lambda p: p[1] not in occupied_emojis, enumerate(self.emojis))
                return InlineKeyboardMarkup(chunks([InlineKeyboardButton(text=e, callback_data=str(i)) for i, e in available_emojis], 6))
            
            userlist = lambda: [f"@{u['username']} : {u['emoji']}" for u in session.players.values()]

            msg = self.npc.bot.send_message(
                chat_id=session.chat_id,
                text=self.text,
                parse_mode=ParseMode.HTML,
                reply_markup=emoji_keyboard()
            )

            def meet_player(update: telegram.Update, context):
                user = update.effective_user
                emoji = self.emojis[int(update.callback_query.data)]

                update.callback_query.answer(f"Приятно познакомиться {emoji}")

                session.players[user.id] = {
                    'username': user.username,
                    'emoji': emoji
                }

                players_emojis = "\n".join([f"@{u['username']} : {u['emoji']}" for u in session.players.values()])

                msg.edit_text(
                    self.text + "\n\n" + players_emojis,
                    parse_mode=ParseMode.HTML,
                    reply_markup=emoji_keyboard()
                )

            def _bind(session: AbstractSession, resume: Callable):
                session.meet_handler = CallbackQueryHandler(meet_player) # todo filters chat
                session.ready_handler = CommandHandler('done', lambda u, c: resume(), filters=Filters.chat(session.chat_id))
                # todo ready handler which removes buttons and pins emojis

                self.npc.dispatcher.add_handler(session.meet_handler)
                self.npc.dispatcher.add_handler(session.ready_handler)

            def _remove(session: AbstractSession):
                self.npc.dispatcher.remove_handler(session.meet_handler)
                self.npc.dispatcher.remove_handler(session.ready_handler)

            return Performance.BIND(_bind, _remove)


@methodize
@dataclass
class Ability:
    name: str
    npc: NPC

    @dataclass
    class Advice(AbstractAction, Method):
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
        bar = value * "#" + "." * (self.total - value)
        return f"Шкала актуальности: <code>[{bar}]</code>"

    @dataclass
    class Instantiate(AbstractAction, Method):

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
    class Add(AbstractAction, Method):

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
