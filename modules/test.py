from engine.glide import StoryMap
from engine.var import Var

from modules.init import npc, score, modules_info

content = StoryMap(
    entry=[
        score.instantiate(),
        npc.Squirrel.say("Пусть каждый тестировщик пришлет стикер. По итогу отправьте *Готово*"),
        npc.Squirrel.acquaintance(
            reply_phrases=["ОК"]),
        npc.Squirrel.say("""Это режим тестирования! Дополнительные команды:
/addscore X - добавить X очков
/vars - вывести значения всех переменных"""),
        npc.Squirrel.ask("Модуль:", modules_info, Var.module)
    ]
)
