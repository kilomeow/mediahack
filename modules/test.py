from engine.glide import StoryMap
from engine.var import Var
from engine.test import Raise

from modules.init import npc, score, modules_info

content = StoryMap(
    entry=[
        Raise('Test error'),
        score.instantiate(),
        npc.Squirrel.say("Пусть каждый тестировщик пришлет стикер. По итогу отправьте *Готово*"),
        npc.Squirrel.acquaintance("/done", "🐶🐱🐭🐹🦊🐻🐼🐨🐯🦁🐮🐷🐸🐵🐔🐧🐺🦄"),
        npc.Squirrel.info("test"),
        npc.Squirrel.say("""Это режим тестирования! Дополнительные команды:
/addscore X - добавить X очков
/vars - вывести значения всех переменных""")
    ]
)
