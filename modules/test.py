from engine.glide import StoryMap
from engine.var import Var

from modules.init import npc, score, docs

content = StoryMap(
    entry=[
        score.instantiate(),
        npc.Squirrel.task(text=f"Вот [сообщение]({docs['fox_note']}). Жду ваших вариантов! Подсказка: удалить нужно всего 4 фрагмента. Каких?",
                          minutes=10,
                          fragments=['Сорока', 'кролик Игорь', 'Пихтовой', 'Медведем'],
                          wrong_fragment='Кажется, это не то, что нужно. Подумайте ещё!',
                          too_big_fragment='Фрагмент правильный, но вы выбрали его избыточно. Попробуйте взять поменьше',
                          correct_fragment='Принято!',
                          left_fragments={3: 'В точку! Осталось ещё 3 слова', 
                                          2: 'Да, да и ещё раз да! Осталось 2 слова',
                                          1: 'Даа! Осталось последнее слово, ну же!', 
                                          0: 'Ееее'}),
        npc.Squirrel.say("Пусть каждый тестировщик пришлет стикер. По итогу отправьте *Готово*"),
        npc.Squirrel.acquaintance(
            reply_phrases=["ОК"]),
        npc.Squirrel.say("""Это режим тестирования! Дополнительные команды:
/addscore X - добавить X очков
/vars - вывести значения всех переменных""")
    ]
)
