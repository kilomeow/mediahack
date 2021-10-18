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
from session_db import push_snapshot


# NarrativeMachine tools

def reading_pause(session):
    if hasattr(session.last_action, 'reading_length'):
        delay = session.last_action.reading_length / reading_speed
        time.sleep(delay)

def play_prefix(session, action):
    push_snapshot(session)
    reading_pause(session)

def debug_prefix(session, action):
    print(f"{session.chat_id}: {action}")


# util functions for checking initial conditions

def check_bots(chat, *bots):
    missing = list()
    for bot in bots:
            try:
                cm = chat.get_member(bot.id)
            except:
                missing.append(bot.name)
            else:
                if cm.status == 'left': missing.append(bot.name)
    return missing

def check_rights(chat, bot, required):
    missing = list()
    bot_member = chat.get_member(bot.id)
    for right in required:
        if not getattr(bot_member, right):
            missing.append(right)
    return missing

def text_cb(text):
    def cb(update, context):
        update.message.reply_text(text)
    return cb

# callbacks

def game_info(update, context):
    update.message.reply_text("Привет! Это игра *Взлом медиа*, кооперативная игра в телеграме, которая познакомит вас с базовыми принципами информационной безопасности. "
"Мы ее проводим вместе с другими ботами — моими коллегами по журналу «Сорокин хвост». С ними вы познакомитесь, когда начнете играть. \n\n"
"Чтобы запустить игру, вам нужно создать групповой чат и добавить туда меня и других игроков. "
"Продолжительность игры займёт *от часа до двух* и зависит от того сколько модулей вы решите пройти. "
"Рекомендуемое количество игроков для прохождения *от 3 до 6*, но игру можно пройти и *в одиночку*. \n\n"
"Когда закончите приготовление, введите команду /start в групповом чате. \n\n"
"Если в ходе прохождения возникнут какие-то сложности, вы можете [написать разработчикам](https://t.me/mediahack_feedback_bot)", parse_mode=ParseMode.MARKDOWN)

def start_game(update, context):
    bot_team = [npc.Floppa.bot, npc.Magpie.bot, npc.Owl.bot]

    missing_bots = check_bots(update.effective_chat, *bot_team)
    missing_rights = check_rights(update.effective_chat, npc.Squirrel.bot, ['can_pin_messages', 'can_restrict_members'])

    context.chat_data['play_allowed'] = not missing_bots and not missing_rights

    rights_locale = {
        'can_pin_messages': 'закрепление сообщений',
        'can_restrict_members': 'бан пользователей'
    }

    instructions = list()
    if missing_bots:
        instructions.append(f"Добавьте {' '.join(missing_bots)} в этот чат")
    if missing_rights:
        instructions.append(f"Назначьте меня администраторкой с правами на {' и '.join(['<b>'+rights_locale[r]+'</b>' for r in missing_rights])}")
    instructions.append("Убедитесь, что все, с <b>кем вы собираетесь играть</b>, находятся в чате")
    if not missing_bots and not missing_rights:
        instructions.append("Введите команду /play !")


    npc.Squirrel.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вы запустили игру <b>Взлом медиа</b>. Эта игра познакомит вас с базовыми принципами информационной безопасности. "
"Продолжительность игры займёт <b>от часа до двух</b> и зависит от того, сколько модулей вы решите пройти. "
"Игра не хранит ваши персональные данные, но собирает данные о прохождении -- "
"Если в ходе прохождения возникнут какие-то сложности, вы можете <a href='https://t.me/mediahack_feedback_bot'>написать разработчикам</a>. "
"Чтобы начать игру:\n\n" + "\n\n".join(map(lambda s: "• "+s, instructions)),
        parse_mode=ParseMode.HTML)


def play(update, context):
    if context.chat_data.get('play_allowed'):
        return play_setup(update, context)

def play_setup(update, context):

    context.chat_data['play_allowed'] = False

    session = BaseSession()
    session.chat_id = update.effective_chat.id
    session.abilities = list()

    session.debug = False

    machine = NarrativeMachine(
        session=session,
        glide_map=modules.intro.content,
        prefix_callback=play_prefix,
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
        prefix_callback=play_prefix,
        error_callback=debug_error,
        end_callback=jump_to_module
    )

    machine.run()

def jump_to_module(session):
    module = getattr(modules, session.var.module)

    machine = NarrativeMachine(
        session=session,
        glide_map=module.content,
        prefix_callback=play_prefix,
        error_callback=debug_error,
        end_callback=ask_module
    )

    machine.run()

# info
npc.Squirrel.dispatcher.add_handler(CommandHandler('start', game_info, filters=Filters.chat_type.private))
npc.Floppa.dispatcher.add_handler(CommandHandler('start', text_cb("По всем вопросам обращайтесь к @squirrel_manager_bot !"), filters=Filters.chat_type.private))
npc.Magpie.dispatcher.add_handler(CommandHandler('start', text_cb("По всем вопросам обращайтесь к @squirrel_manager_bot !"), filters=Filters.chat_type.private))
npc.Owl.dispatcher.add_handler(CommandHandler('start', text_cb("По всем вопросам обращайтесь к @squirrel_manager_bot !"), filters=Filters.chat_type.private))
npc.Rabbit.dispatcher.add_handler(CommandHandler('start', text_cb("По всем вопросам обращайтесь к @squirrel_manager_bot !"), filters=Filters.chat_type.private))

npc.Squirrel.dispatcher.add_handler(CommandHandler('start', start_game, filters=Filters.chat_type.groups))
npc.Squirrel.dispatcher.add_handler(CommandHandler('play', play, filters=Filters.chat_type.groups))

if __name__ == '__main__':
    for updater in updaters:
        updater.start_polling()
