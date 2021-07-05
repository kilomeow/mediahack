from engine.glide import StoryMap
from engine.var import Var, Let, Conditional, Proceed, Jump

from modules.init import npc, ab, score

description = "Фишинг, VPN и почты"

content = StoryMap(
    entry = [
        npc.Magpie.say("ребята кажется я нашла кое-что новое о пожарах но мне нужна помощь"),
        npc.Floppa.say("ВАУ"),
        npc.Magpie.say("прост мне пришло загадочное письмо на почту и кажется со мной хотят поговорить о пожарной службе"),
        npc.Magpie.say("там что-то нечисто"),
        npc.Floppa.say("Чем мы можем тебе помочь???"),
        npc.Magpie.say("мне нужно продолжить переписку но я не знаю как именно"),
        npc.Magpie.say("мой собеседник не хочет чтобы что то пошло не так"),
        npc.Magpie.say("я не могу его сейчас подставить понимаете???"),
        npc.Owl.say("Вы только почтой пользуетесь?"),
        npc.Magpie.say("да"),
        npc.Owl.say("А впн есть?"),
        npc.Floppa.say("Я раньше квн смотрел, сейчас там шутки вообще не смешные...."),
        npc.Owl.say("НЕ КВН А ВПН"),
        npc.Owl.info("VPN - это виртуальная частная сеть, то есть незримый кабель, который протягивается в вашу удалённую сеть через интернет, идущий поверх защищённого соединения."),
        npc.Magpie.say("очень понятно"),
        npc.Owl.say("Дотянуться до такого кабеля очень тяжело, поэтому он может привести вас к заблокированным сайтам и сервисам, а увести ваш траффик из него будет крайне тяжело."),
        npc.Floppa.say("А кто протягивает этот кабель? Один конец у меня, понятно, а где второй? Или он бесконечный? "),
        npc.Owl.say("Второй конец кабеля, если не вдаваться в подробности, присоединён к серверу, который заменяет ваш IP на свой. Таким образом, VPN позволяет пользователю обходить блокировки и защищает от отслеживания."),
        npc.Magpie.say("хмм"),
        npc.Owl.say("Но есть одно но: vpn-сервисов очень много, и сейчас многие из них активно блокируются. "),
        npc.Owl.info("VPN бывает либо платным, либо бесплатным. В первом случае вам нужно действительно тратить деньги из своего кармана, но зато вы точно знаете, кто именно отвественнен за ваше соединение, а во втором вы серьёзно рискуете своей безопасностью, связываясь с чужим сервером без всяких гарантий."),
        npc.Magpie.say("то есть если у меня нет денег то я остаюсь в голым хвостом?"),
        npc.Owl.info("Почти так. Но для защиты наших хвостов есть Tor, он сверхзащищённый, полностью бесплатный, но суперсложный. Он похож на луковицу, в которой каждый слой зашифрован отдельно от предыдущего и последующего. В целом же у него очень сложная структура, которая нужна для одного - для обеспечения защищённости и анонимности."),
        npc.Magpie.say("всё это очень интересно но вообще я изначально про ПОЧТУ спрашивала"),
        npc.Owl.say("Так вот. VPN тебе будет необходим, если ты захочешь воспользоваться защиentryщённой почтой. Вот как раз ProtonMail сейчас заблокирован в российских лесах, и к нему без VPN не подобраться."),
        npc.Magpie.say("вот теперь стало легче"),
        npc.Magpie.say("сначала луковицы теперь протоны"),
        npc.Owl.info("ProtonMail - это не просто почта. Это почта со сквозным шифрованием. Все письма, отправляемые в протона шифруются ключом, который доступен только отправителю и получателю."),
        npc.Owl.info("Если же письмо отправляется с протона на другой почтовый сервис, то отправитель должен передать ключ шифрования получателю сам. Тут уже вы сами вольны выбирать способ передачи, но помните, что он должен быть максимально безопасным. Например, ключ точно нельзя диктовать по телефону или пересылать по SMS."),
        npc.Floppa.say("Вау! Чувствую себя спецагентом..."),
        npc.Owl.say("Давайте-ка я подключу вас к серверу моих знакомых ящериц из Калифорнии!"),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.say("**[Включить VPN]**"),
        npc.Floppa.say("Блин, теперь в твиттере все думают, что я калифорнийский кот("),
        npc.Magpie.say("так я подключила этот ваш протон мэйл "),
        npc.Magpie.say("сейчас свяжусь с информатором"),
        npc.Magpie.say("есть!"),
        npc.Magpie.say("просто прочитайте очень странная история"),
        npc.Magpie.say("**сообщение от информатора**"),
        npc.Floppa.say("Они вырубили не те деревья и что?"),
        npc.Magpie.say("а то"),
        npc.Magpie.say("это незаконно"),
        npc.Magpie.say("вопрос в том стоит ли публиковать это сообщение"),
        npc.Magpie.say("скан в письме выглядит нормальным "),
        npc.Magpie.say("но я не уверена до конца"),
        npc.Squirrel.say("Действительно! "),
        #В СТРОКЕ НИЖЕ ДОЛЖНО БЫТЬ ГОЛОСОВАНИЕ
        npc.Squirrel.ask(
            "Ребята, внимание! Нам сейчас нужно решить, что делать с этим материалом. Сейчас у нас нет возможности его проверить, поэтому в случае публикации мы можем нарваться не неприятности. С другой стороны, мы можем привлечь ещё больше внимания к пожарам.",
            [("Публикуем", "published"), ("Не публикуем", "not_published")], Var.publish_material),
        Jump(Var.publish_material)
    ],

    published = [
        #    - ПОСЛЕДСТВИЯ: Публикуем

        npc.Magpie.say("хорошо сейчас я уберу из документа всё лишнее чтобы сделать нашего информатора анонимным"),
        npc.Magpie.say("готово!"),
        #В СТРОКЕ НИЖЕ ПОЯВЛЯЕТСЯ ШКАЛА!
        score.add(3),
        npc.Owl.say("Вау, пожарная служба вывесила на сайте опровержение"),
        npc.Squirrel.say("Да, у нас могут быть проблемы "),
        npc.Squirrel.say("Будем следить за развитием событий и думать вместе!"),
        Proceed(letter = True),
    ],

    not_published = [
        #    - ПОСЛЕДСТВИЯ: Не публикуем

        npc.Magpie.say("ладно я попробую раздобыть что-то ещё"),
        npc.Magpie.say("но я не уверена что у меня получится"),
        npc.Floppa.say("Не переживай! Ты обязательно всё сможешь!"),
        npc.Squirrel.say("Может быть, с ты сможешь ещё с кем-нибудь связаться!"),
        # ЗДЕСЬ КОНЕЦ ПОСЛЕДСТВИЙ
        Proceed(letter = True),
    ],

    letter = [
        npc.Magpie.say("эй Сова"),
        npc.Magpie.say("я тут зашла на редакционную почту"),
        npc.Magpie.say("тут какое-то письмо про конференцию это не ты заявку отправляла?"),
        npc.Magpie.say("там надо по ссылке зарегаться я сейчас нас всех оформлю ок?"),
        npc.Owl.say("ПОДОЖДИ"),
        npc.Owl.say("Покажи письмо"),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Magpie.say("[Посмотреть письмо]"),
        npc.Magpie.say("**фишинговое письмо**"),
        npc.Floppa.say("Выглядит нормально"),
        npc.Floppa.say("Кажется, кто-то из нас слишком много работает"),
        npc.Owl.say("Говорю вам, тут что-то не так, клювом чувствую"),
        # ЗДЕСЬ     - ДЕЙСТВИЕ: Посмотреть тему письма

        npc.Magpie.say("Приглашение на 5-ую конференцию лесных изданий"),
        npc.Magpie.say("в прошлом году была 4-ая конференция значит в этом году должна быть пятая"),
        npc.Floppa.say("Логично"),
        # ЗДЕСЬ     - ДЕЙСТВИЕ: Посмотреть текст письма

        npc.Magpie.info("Начало конференции было перенесено на 21 августа, окончание запланировано на 27 августа. В эти дни запланировано выступление спикеров, среди которых павиан Антуан, куница Эрика и филин Вячеслав, а так же мастер-классы по организации работы в условиях пожаров, загрязнения воды тяжёлыми металлами и других угроз."),
        npc.Magpie.say("хмм тут есть перечень спикеров и расписание"),
        npc.Floppa.say("Антуана и Эрику я знаю, они классные! "),
        npc.Floppa.say("А что за филин?"),
        npc.Owl.say("Понятия не имею. Русскоязычное совиное сообщество достаточно тесное, но я его не встречала"),
        npc.Squirrel.say("Смотрите!"),
        npc.Squirrel.say("В последнем предложении есть опечатка!"),
        npc.Floppa.say("Может, они устали печатать?"),
        npc.Squirrel.say("А вот и нет, такие сообщения не набираются каждый раз вручную"),
        npc.Owl.say("БАЦ"),
        # ЗДЕСЬ     - ДЕЙСТВИЕ: Посмотреть на ссылку в письме

        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Magpie.say("Зарегистрироваться и ознакомиться со списком запланированных мероприятий можно по ссылке: **[link]**"),
        npc.Owl.say("У ссылки подозрительный домен"),
        npc.Owl.say("Это не похоже на официальный сайт конференции, тут ошибка в названии!"),
        npc.Floppa.say("Блииин"),
        npc.Owl.say("Коллеги, это фишинговое письмо"),
        npc.Floppa.say("Но мы же не рыбы..."),
        npc.Owl.say("Фишинг не имеет отношения к рыбалке. Это способ получить доступ к данным пользователя, используя его невнимательность. Если бы мы сейчас перешли на сайт, авторизировались и прошли регистрацию на конфу, наши пароли и прочее просто бы увели."),
        npc.Floppa.say("А как ты поняла, что это фишинговое письмо??"),
        npc.Owl.info("У фишинговых писем есть несколько особенностей. Первое - сам вид фишинговых ссылок, частно они похожи на настоящиие, но в них могут быть опечатки в протоколах, доменах и названиях. Второе - это наличие опечаток в письме. Белка права, настоящие письма всегда заполняются через форму, в них опечаток нет. И третье: помните спикеров в письме и тему? Они попытались нас запутать, указав в письме реальное событие и реальных зверей. Правда, им это не совсем удалось."),
        #В СТРОКЕ НИЖЕ ДОЛЖНО БЫТЬ ГОЛОСОВАНИЕ
        npc.Squirrel.ask(
            "Всё, что я сейчас поняла, это то, что наши данные пытались своровать. Нам стоит рассказать об этом случае нашим читателям?",
            [("Сообщаем", "reported"), ("Не сообщаем", "not_reported")], Var.report_to_readers),
        Jump(Var.report_to_readers),
        Proceed(ending_junction = True)
    ],

    reported = [
        #    - ПОСЛЕДСТВИЯ: Сообщаем

        npc.Magpie.say("еее я подготовила заметку"),
        npc.Magpie.say("готово!"),
        #В СТРОКЕ НИЖЕ ПОЯВЛЯЕТСЯ ШКАЛА!
        score.add(3),
        npc.Squirrel.say("В комметариях читатели люто негодуют"),
        npc.Floppa.say("И правильно"),
    ],

    not_reported = [
        #    - ПОСЛЕДСТВИЯ: Не сообщаем

        npc.Magpie.say("лады"),
        npc.Magpie.say("я тоже думаю что это не сильно важная новость"),
        npc.Owl.say("Это как посмотреть"),
        npc.Owl.say("Такое не каждый день случается"),
        # ЗДЕСЬ КОНЕЦ ПОСЛЕДСТВИЙ
    ],

    ending_junction = [
        Conditional(
            ending1=lambda var: var.report_to_readers and var.publish_material,
            ending2=lambda var: var.report_to_readers,
            ending3=lambda var: var.report_to_readers or not (var.report_to_readers and var.publish_material)
        )
    ],

    ending1 = [
        # ЗДЕСЬ     - КОНЦОВКА: Всё опубликовано

        npc.Magpie.say("ВЫ ВИДЕЛИ ЧТО СЕЙЧАС ОПУБЛИКОВАЛИ ДРОЗДЫ"),
        npc.Magpie.say("**сообщение дроздов**"),
        npc.Floppa.say("ВАУ"),
        npc.Floppa.say("Серьёзно???"),
        npc.Squirrel.say("Нам нужно помочь дроздам! Надо поделиться их заявлением!"),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Squirrel.say("[Опубликовать сообщение]"),
        #В СТРОКЕ НИЖЕ ПОЯВЛЯЕТСЯ ШКАЛА!
        score.add(2),
        npc.Magpie.say("кажется наши последние публикации привлекли внимание полиции"),
        npc.Floppa.say("Это плохо?"),
        npc.Magpie.say("смотрите что выкатила их пресс-служба!!!!!"),
        npc.Magpie.say("**заявление пресс-службы**"),
        npc.Floppa.say("ДА ЛАДНО"),
        npc.Magpie.say("я в шоке"),
        npc.Floppa.say("Какие же мы крутые!!!"),
        npc.Squirrel.say("Такое редко случается, но уши надо держать востро!"),
        npc.Squirrel.say("А сейчас можно выдохнуть спокойно"),
    ],

    ending2 = [
        # ЗДЕСЬ     - КОНЦОВКА: Опубликовано только сообщение информатора:

        npc.Magpie.say("ВЫ ВИДЕЛИ ЧТО СЕЙЧАС ОПУБЛИКОВАЛИ ДРОЗДЫ"),
        npc.Magpie.say("**сообщение дроздов**"),
        npc.Floppa.say("ВАУ"),
        npc.Floppa.say("Серьёзно???"),
        npc.Squirrel.say("Нам нужно помочь дроздам! Надо поделиться их заявлением!"),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Squirrel.say("[Опубликовать сообщение]"),
        #В СТРОКЕ НИЖЕ ПОЯВЛЯЕТСЯ ШКАЛА!
        score.add(2),
        npc.Magpie.say("будем готовиться к мега крутому расследованию!"),
        npc.Floppa.say("Отличная работа!!!!"),
        npc.Squirrel.say("Нам всем сейчас лучше передохнуть немного"),
        npc.Squirrel.say("фух"),
    ],

    ending3 = [
        # ЗДЕСЬ     - КОНЦОВКА: Ничего не опубликовано или опубликовано только сообщение про фишинг

        npc.Squirrel.say("Меня всё это дико напрягает"),
        npc.Squirrel.say("Кажется,  дальше будет очень тяжело"),
        npc.Floppa.say("Мы справимся!!!"),
        npc.Magpie.say("почему надо всегда делать нам какие-то пакости????"),
        npc.Floppa.say("Зверь зверю - волк...."),
        npc.Magpie.say("вообще так ток про людей говорят"),
        npc.Squirrel.say("Давайте лучше успокоимся и выдохнем, хорошо")
    ]

)
