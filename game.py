from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.inlinequeryhandler import InlineQueryHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.parsemode import ParseMode
from engine.core import NarrativeMachine
from engine.basic import BaseSession

# engine actions
from engine.glide import StoryMap
from engine.telegram_npc import NPC, Ability
from engine.var import Var, Let, Conditional, Proceed

# telegram
from telegram.ext import CommandHandler, Updater, dispatcher, Filters
from telegram import Update

# setting up
from modules.init import npc, ab, updaters, abilities_names

import modules.intro.entry

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
        text="Вы выбрали:\n"+ "\n".join([f"<b>{a}</b>" for a in session.abilities]) + "\n\n" + "Напишите Готово чтобы продолжить",
        parse_mode=ParseMode.HTML,
        reply_markup=inline_row(*remaining_abs))
    

ab_handler = CallbackQueryHandler(update_abs)

#npc.Squirrel.dispatcher.add_handler(ab_handler)

actions_delay = 1

import time

def action_prefix(session, action):
    time.sleep(actions_delay)
    print(f"{session.chat_id}: {action}")


def setup(update, context):
    session = BaseSession()
    session.chat_id = update.effective_chat.id
    session.abilities = list()
    context.chat_data['session'] = session    

    machine = NarrativeMachine(
        session=context.chat_data['session'],
        glide_map=modules.intro.entry.content,
        prefix_callback=action_prefix,
        error_callback=lambda e, s, p, a: print(type(e), e, s, p, a),
        end_callback=lambda s: print('End!')
    )
    
    machine.run()

npc.Squirrel.dispatcher.add_handler(CommandHandler('start', setup))

npc.Squirrel.dispatcher.add_handler(MessageHandler(Filters.regex("^(Готово)$"), setup))


if __name__ == '__main__':
    for updater in updaters:
        updater.start_polling()
