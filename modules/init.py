# engine actions
from engine.telegram_npc import NPC, Ability, Score

# telegram
from telegram.ext import Updater


import json

from types import SimpleNamespace

npc = SimpleNamespace()
ab = SimpleNamespace()

updaters = list()
abilities_names = list()

with open('config.json') as config_f:
    conf = json.load(config_f)

with open('modules/stickers.json') as stickers_f:
    stickerset = json.load(stickers_f)

for c in conf['characters']:
    updater = Updater(c['token'])

    updaters.append(updater)

    setattr(npc, c['var'], NPC(typing_speed=c['typing_speed'],
                            bot=updater.bot,
                            dispatcher=updater.dispatcher,
                            stickerset=stickerset))

for a in conf['abilities']:
    setattr(ab, a['var'], Ability(name=a['name'],
                                    npc=getattr(npc, a['npc']) ))
    abilities_names.append(a['name'])

score = Score(total=15, manager=npc.Squirrel)

reading_speed = conf['reading_speed']

with open('modules/docs.json') as docs_f:
    docs = json.load(docs_f)

import modules
import modules.intro
import modules.fishing
import modules.media
import modules.hacking
import modules.encryption

modules_names = ['fishing', 'hacking', 'encryption']
modules_info = [(getattr(modules, n).description, n) for n in modules_names]

entry_module = 'intro'

modules_deps = {
    'intro': {
        'requires': [],
        'blocked_by': []
    },

    'media': {
        'requires': ['intro'],
        'blocked_by': ['hacking']
    },

    'hacking': {
        'requires': ['intro'],
        'blocked_by': []
    },

    'encryption': {
        'requires': ['intro', 'hacking'],
        'blocked_by': []
    },

    'fishing': {
        'requires': ['intro'],
        'blocked_by': []
    }
}