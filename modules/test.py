from engine.glide import StoryMap
from engine.var import Var, Let, Conditional, Proceed, Jump

from modules.init import npc, ab, score, docs, modules_info

content = StoryMap(
    entry = [
        score.instantiate(),
        npc.Squirrel.info("""Это режим тестирования! Дополнительные команды:
/addscore X - добавить X очков
/vars - вывести значения всех переменных"""),
        npc.Squirrel.ask("Модуль:", modules_info, Var.module)
    ]
)
