from telegram import parsemode
import telegram
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.inlinequeryhandler import InlineQueryHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.parsemode import ParseMode
from engine.core import NarrativeMachine
from engine.basic import BaseSession

import time

# engine actions
from engine.glide import StoryMap
from engine.telegram_npc import NPC, Ability
from engine.var import Var, Let, Conditional, Proceed, VarSession

# telegram
from telegram.ext import CommandHandler, Updater, dispatcher, Filters
from telegram import Update

# setting up
from modules.init import npc, ab, updaters, abilities_names, score, reading_speed, modules_info, conf

# start modules
import modules.intro
import modules.test



def inline_row(*text_seq):
    buttons = [InlineKeyboardButton(text=t, callback_data=t) for t in text_seq]
    return InlineKeyboardMarkup.from_row(buttons)


def init(update, context):
    session = BaseSession()
    session.chat_id = update.effective_chat.id
    session.abilities = list()
    context.chat_data['session'] = session
    update.message.reply_text("Выберите две способности вашей команды:",
                              reply_markup=inline_row(*abilities_names))


def update_abs(update: Update, context):
    ability = update.callback_query.data
    update.callback_query.answer(text=f"Берем {ability}")

    session = context.chat_data['session']
    session.abilities.append(ability)

    if len(session.abilities) > 2:
        session.abilities.pop(0)

    remaining_abs = [a for a in abilities_names if a not in session.abilities]

    update.callback_query.message.edit_text(
        text="Вы выбрали:\n" + "\n".join([f"<b>{a}</b>" for a in session.abilities]) + "\n\n" +
             "Напишите Готово чтобы продолжить",
        parse_mode=ParseMode.HTML,
        reply_markup=inline_row(*remaining_abs))


ab_handler = CallbackQueryHandler(update_abs)

# npc.Squirrel.dispatcher.add_handler(ab_handler)


def reading_pause_prefix(session, action):
    if hasattr(session.last_action, 'reading_length'):
        delay = session.last_action.reading_length / reading_speed
        time.sleep(delay)


def debug_prefix(session, action):
    print(f"{session.chat_id}: {action}")


def start(update, context):
    # todo check bots
    npc.Squirrel.bot.send_message(
    chat_id=update.effective_chat.id,
    text="""
Вы запустили игру «Взлом медиа». Эта игра познакомит вас с базовыми правилами кибербезопасности.
Продолжительность игры займёт примерно час, но зависит от того сколько модулей вы решите пройти.
1) Убедитесь что в чате есть @floppa_foundation_bot @crypto_owl_bot @magpie_reporter_bot
2) Проверьте, что у меня есть права администратора
3) Введите команду /play чтобы начать играть!""")

    npc.Squirrel.dispatcher.add_handler(CommandHandler('play', play_setup))
    if conf['dev']: npc.Squirrel.dispatcher.add_handler(CommandHandler('test', test_setup))



def play_setup(update, context):
    session = BaseSession()
    session.chat_id = update.effective_chat.id
    session.abilities = list()

    session.debug = False

    machine = NarrativeMachine(
        session=session,
        glide_map=modules.intro.content,
        prefix_callback=reading_pause_prefix,
        error_callback=lambda e, s, p, a: print(type(e), e, s, p, a),
        end_callback=ask_module
    )

    machine.run()


def test_setup(update: telegram.Update, context):
    session = BaseSession()
    session.chat_id = update.effective_chat.id
    session.abilities = list()
    session.var._data['null'] = None
    session.players = list()

    session.debug = True

    def addscore(update, context):
        v = int(update.message.text.split()[1])
        action = score.add(v)
        action.perform(session)

    def vars(update, context):
        update.message.reply_text(
            "\n".join([f"<code>Var.{var}</code> : {val}" for var, val in session.var._data.items()]),
            parse_mode=ParseMode.HTML
        )

    npc.Squirrel.dispatcher.add_handler(CommandHandler('addscore', addscore, filters=Filters.chat(session.chat_id)))
    npc.Squirrel.dispatcher.add_handler(CommandHandler('vars', vars, filters=Filters.chat(session.chat_id)))

    machine = NarrativeMachine(
        session=session,
        glide_map=modules.test.content,
        prefix_callback=debug_prefix,
        error_callback=debug_error,
        end_callback=ask_module
    )

    machine.run()


module_choose = StoryMap(
    entry = [
        npc.Squirrel.ask("Выберите модуль, который вы хотите пройти",
            modules_info,
            Var.module)
    ]
)

def debug_error(error, state, progress, session, action):
    npc.Squirrel.bot.send_message(chat_id=session.chat_id,
    text=f"<code>{state}:{progress}</code>\n"+
         f"<code>{error.__class__.__name__}</code>\n"+
         f"<code>{error}</code>",
    parse_mode=ParseMode.HTML)

def ask_module(session: VarSession):
    machine = NarrativeMachine(
        session=session,
        glide_map=module_choose,
        prefix_callback=debug_prefix if session.debug else reading_pause_prefix,
        error_callback=debug_error,
        end_callback=jump_to_module
    )

    machine.run()

def jump_to_module(session):
    module = getattr(modules, session.var.module)

    machine = NarrativeMachine(
        session=session,
        glide_map=module.content,
        prefix_callback=debug_prefix if session.debug else reading_pause_prefix,
        error_callback=debug_error,
        end_callback=ask_module
    )

    machine.run()


npc.Squirrel.dispatcher.add_handler(CommandHandler('start', start))

if __name__ == '__main__':
    for updater in updaters:
        updater.start_polling()
