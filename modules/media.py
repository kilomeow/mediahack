from engine.glide import StoryMap
from engine.var import Var, Let, Conditional, Proceed, Jump

from modules.init import npc, ab, score, docs

description = "Социальные сети и мессенджеры"

content = StoryMap(
    entry = [
        npc.Squirrel.say("Сорока, вы там готовы?"),
npc.Magpie.say("да мы почти закончили"),
npc.Floppa.say("УРА"),
npc.Floppa.say("Это ведь материалы про лагерь погорельцев, в котором работает Кролик, да??"),
npc.Rabbit.say("так точно"),
npc.Rabbit.say("мы на месте ещё"),
npc.Floppa.say("Как там сейчас?"),
npc.Rabbit.say("если честно, то очень тяжело"),
npc.Rabbit.say("здесь очень много пострадавших, и у нас проблемы с водой"),
npc.Floppa.say("Жеееесть сил вам!!"),
npc.Rabbit.say("спасибо!"),
        npc.Squirrel.say("ВНИМАНИЕ"),
        npc.Squirrel.say("Жду редактуру! Нужно сделать источники анонимными, если они есть, и убрать авторские примечания в скобках"),
        npc.Squirrel.say(docs['note1']),
        npc.Floppa.say("Да! И не забывайте советоваться друг с другом в чятике"),
        npc.Floppa.say("Копандная работа это не пельмени варить"),
        npc.Floppa.say("Хотя..."),
        npc.Squirrel.say("Мне сейчас срочно надо резвесить грибы сушиться"),
        npc.Squirrel.ask("Напишите готово, когда закончите, и я тут же вернусь", [("Готово", "ready")], Var.null),

        score.add(3),

        npc.Magpie.say("тут нам прислали кое-что"),
        npc.Floppa.say("ЧТО?????"),
        npc.Magpie.say("кое-что неприятное"),
        npc.Magpie.say("я не уверена что новеньким стоит это читать"),
        npc.Floppa.say("Там что-то жуткое?"),
        npc.Magpie.say("вы новенькие меня поймите я тут давно уже и всякого насмотрелась"),
        npc.Magpie.say("но мне бы не хотелось, чтобы вы воспринимали это как-то близко к сердцу"),
        npc.Floppa.say("ДА ЧТО ТАМ"),
        npc.Magpie.ask("хорошо но не пугайтесь особо", [("Посмотреть", "ready")], Var.null),
        npc.Magpie.info("""Вы хотели привлечь внимание и вы его привлекли. Не все здесь хотят видеть немытых мигрантов у себя под окнами. 
Скажите вашим пушистым друзьям, чтобы сворачивали свои палатки и шли в другое место, пока мы их не нашли. Мы не станем кормить их за свой счет. Ровно так же, как и вашу газетёнку.

Прекращайте этот балаган немедленно. """),
        npc.Rabbit.say("вот об этом я и говорил"),
        npc.Squirrel.say("Так, и что делаем? Мы продолжаем?"),
        npc.Rabbit.say("ну я пока ничего страшного не вижу"),
        npc.Rabbit.say("чем больше зверей узнают о нас, тем лучше"),
        npc.Magpie.say("зверей и птиц прошу заметить"),
        npc.Rabbit.say("так, ещё"),
        npc.Rabbit.say(docs["note2"]),
        npc.Rabbit.say("вот этот текст вычитайте прям очень внимательно, пожалуйста, я торопился и мог что-то проглядеть"),
        npc.Squirrel.say("Работаем! "),
        npc.Squirrel.say("Ребята-зверята, Кролик не убрал пару примечаний за собой, найдите их и уберите, пожалуйста."), 
        npc.Squirrel.ask('Закончили?', [("Готово", "ready")], Var.null),

        score.add(3),
        npc.Magpie.say(".........."),
        npc.Magpie.say("они не унимаются"),
        npc.Magpie.say("видимо нас читают бескультурные звери которым нечем заняться "),
        npc.Magpie.say("нам в бота снова присылают гадости"),
        npc.Magpie.say("теперь тут прямо лично про меня"),
        npc.Magpie.ask("очень мерзко", [("Посмотреть", "ready")], Var.null),
        npc.Magpie.info("""Привет, Сорока!
Я уже купил спички и собираюсь устроить пикник недалеко от леса! Скажи ты любишь загорать? Если да то тебе понравится гореть будет очень ярко! А потом я обязательно зайду к вам в гости я слышал что вы любите вские горячие новости а будет очень горячо....

З.Ы. Передавай обгоревшим уродам привет"""),
        npc.Rabbit.say("забей"),
        npc.Rabbit.say("это тупо какой-то третьеклассник писал"),
        npc.Floppa.say("Буквы в интернете ещё никого не убивали"),
        npc.Magpie.say("ну это как посмотрет"),
        Proceed(photo = True)
    ],

    photo = [
        npc.Rabbit.say("а вот сейчас я реально напрягся"),
        npc.Rabbit.say("выложил в инсту фотографию лагеря, и в комменты набежали какие-то типы"),
        npc.Rabbit.say("никогда не видел столько хейта"),
        npc.Rabbit.say("пишут, что хотят всё сжечь"),
        npc.Floppa.say("Посмотри на юзернеймы, наверняка боты"),
        npc.Floppa.say("Не переживай, такое часто случается! Даже если это живые люди, такие обычно сидят дома и ничего не делают)"),
        npc.Magpie.say("ТЫ ЗАЧЕМ ВЫЛОЖИЛ "),
        npc.Magpie.say("разве не ты просил меня не писать где лагерьь??"),
        npc.Floppa.say("Да всё нормально! Вряд ли вас кто-то вычислит по веткам))"),
        npc.Magpie.say("уже"),
        npc.Magpie.say("вот что пишут в телеграм-канале Чистый Лес:"),
        npc.Magpie.info("""Мы уже оперативно вычислили всех, кто сочувствует облезлому Сорокиному хвосту. Их имена и адреса установлены, их любимая газётенка даже не думала их спасать.
Мы настоятельно рекомендуем всем, кто хочет открыть свою пасть, немедленно её заткнуть ради своей же безопасности."""),
        npc.Rabbit.say("пусть тольок попроуют я им блин все хвосты повыдёргиваю"),
        npc.Squirrel.say("Спокойно"),
        npc.Squirrel.say("Как они вообще это сделали???"),
        npc.Squirrel.say("Сова, что теперь делать?"),
        npc.Owl.say("Это обычная ситуация, Кролику не стоило выкладывать эту фотографию в общий доступ. Сейчас обнаружить то или иное место по окружению достаточно легко: это может быть и вид из окна, и какое-то строение на фоне, что угодно."),
        npc.Rabbit.say("на фотку попал огромный дуб"),
        npc.Rabbit.say("блин реально его же все в лесу знают"),
        npc.Rabbit.say("как я мог так факапнуться"),
        npc.Rabbit.say("капец"),
        npc.Owl.say("Кролик, бери лапы в лапы и беги к нотариусу. Тебе нужен *«Акт осмотра страницы в сети «Интернет»* двух этих скриншотов с угрозами*.* Жалобу в телеграм я уже отправил, хотя это может ни на что не повлиять."),
        npc.Owl.say("Можно было бы ещё обратиться в полицию, но я не уверена, что они будут что-то предпринимать, тут будем действовать по ситауции"),
        npc.Rabbit.say("мне сейчас рельно нужно бежать к нотариусу???"),
        npc.Owl.say("ДА"),
        npc.Squirrel.say("Да!"),
        npc.Rabbit.say("ладно ладно"),
        npc.Rabbit.say("побежал!!"),
        npc.Squirrel.say("А нам что делать? Тут и про нас есть!"),
        npc.Owl.say("Угрозы редакции тоже укажем в заявлении."),
        npc.Owl.say("А сейчас вы можете сообщить об угрозах читателям, это привлечет внимание. Но с другой стороны, недоброжелателей так тоже можно спровоцировать."),
        npc.Squirrel.say("Нужно подумать, это очень серьёзная ситуация. Давайте проголосуем."),
        npc.Squirrel.ask("У вас только одно нажатие!", [("Сообщаем", "public"), ("Не сообщаем", "not_public")], Var.threat_public),
        Jump(Var.threat_public)
    ],
        # ЗДЕСЬ———————игроки голосуют———————

        #ПОСЛЕДСТВИЯ: Сообщаем

    public = [
        npc.Squirrel.say("Ух"),
        npc.Magpie.say("хорошо! я подготовлю заявление и скоро  отправлю"),
        score.add(2),
        npc.Squirrel.say("У поста очень много просмотров! Наверное, это хорошо..."),
        npc.Floppa.say("Вы молодцы!"),
        npc.Magpie.say("в бот приходит очень много слов поддержки"),
        npc.Magpie.say("мне даже как-то легче стало"),
        npc.Squirrel.say("Это хорошо. А теперь работаем дальше!"),
        Proceed(game_break = True)
    ],

    not_public = [
        npc.Squirrel.say("Ладно, будем следить за ситуацией"),
        npc.Floppa.say("Правильно! Им нельзя давать никакую публичность"),
        npc.Floppa.say("Кролик напишет заявление и пусть полиция с ними говорит"),
        npc.Magpie.say("если заявление вообще примут"),
        npc.Squirrel.say("В любом случае работаем дальше"),
        Proceed(game_break = True)
    ],

    game_break = [
        npc.Squirrel.ask("Самое время взять небольшую паузу! Отдохните, налейте себе чай, дайте себе перевести дыхание. Приступайте только когда почувствуете что есть силы продолжать игру.", [("Продолжить", "next")], Var.null),
        Proceed(vzlom = True)
    ],

    vzlom = [
        npc.Rabbit.say("Здравствуйте, коллеги!"),
        npc.Rabbit.info("С прискорбием сообщаю от лица нашей организации о закрытии лагеря. Эти животные совершенно не хотят жить по правилам, поэтомы мы вынуждены прекратить нашу деятельность."),
        npc.Floppa.say("Чегоо???"),
        npc.Squirrel.say("Эээ."),
        npc.Rabbit.info("Мы просим удалить вас все материалы о нашей организации и лагере. Мы знаем, что это противоречит вашей политике, но мы действительно хотели бы полностью забыть эту историю."),
        npc.Floppa.say("А что с беженцами?"),
        npc.Rabbit.say("Мы перенаправим их в другие убежища. "),
        npc.Squirrel.say("Мы не можем удалять материалы, но мы можем опубликовать ваш комментарий по поводу закрытия шелтера."),
        npc.Floppa.say("Так что же у вас случилось? Кролик, ты же написал заявление??"),
        npc.Rabbit.say("Мы дадим комментарий только в обмен на удаление материалов. К сожалению, никак иначе мы не можем, это нужно в целях безопасности."),
        npc.Floppa.say("А нотариус?"),
        npc.Floppa.say("Кролик?"),
        npc.Floppa.say("Мне это не нравится."),
        npc.Floppa.say("Белка, это очень странно. Кролика могли взломать?"),
        npc.Squirrel.say("Не знаю"),
        npc.Squirrel.say("Мне бы не хотелось, чтобы наша переписка оказалась в чьих-то лапах..."),
        npc.Squirrel.say("Давайте разберемся вместе"),
        #В СТРОКЕ НИЖЕ ДОЛЖНО БЫТЬ ГОЛОСОВАНИЕ
        npc.Squirrel.ask("Подумайте хорошенько перед тем как принимать решение! У вас только одно нажатие на кнопку, обсудите ваши идеи в чате.", [("Кролик взломан", "kick"), ("Кролик не взломан", "notkick")], Var.kick_rabbit),
        Jump(Var.kick_rabbit)
    ],

    kick = [
        npc.Squirrel.kick(npc.Rabbit),
        npc.Squirrel.info("Надеюсь, мы поступили правильно."),
        Proceed(vzlom_advice = True)
    ],

    notkick = [
        npc.Squirrel.say("Ладно, Кролик."),
        npc.Squirrel.say("Сейчас я уберу с сайта заметки."),
        score.add(-2),
        npc.Squirrel.say("..."),
        npc.Squirrel.say("Мне только что позвонили из Нашего Дома"),
        npc.Squirrel.kick(npc.Rabbit),
        npc.Squirrel.say("Кролика всё-таки взломали..."),
        npc.Floppa.say("Ты же можешь вернуть материалы?"),
        npc.Squirrel.say("Конечно, сейчас"),
        npc.Squirrel.say("Блин, нехорошо"),
        npc.Squirrel.say("Я всех подвела"),
        npc.Floppa.say("Вы же никогда с таким не сталкивались! И ты же смогла всё исправить"),
        Proceed(vzlom_advice = True)
    ],

    vzlom_advice = [
        npc.Magpie.say("вот что пишут в  канае Наш Дом:"),
        npc.Magpie.info("""
Привет, это Варвара. Только что трех наших активистов взломали.

Чтобы избежать повторных случаев взлома, мы удаляем все наши аккаунты в соцсетях. Связаться с нами все еще можно по горячей линии.

Мы считаем, что взломы связаны с угрозами от неизвестных, которые регулярно поступают нам с момента открутия лагеря. По факту угроз мы уже написали заявление в полицию.

Спасибо всем за поддержку. Мы обязательно со всем справимся!

Берегите себя.
"""),
        npc.Magpie.say("жуть какая-то"),
        npc.Floppa.say("У вас раньше уже было что-то подобное? Это можно назвать массовым взломом?"),
        npc.Squirrel.say("Вот сейчас я правда начала нервничать"),
        npc.Squirrel.say("Ребят, вы хоть двухфакторкой пользуетесь?"),
        npc.Magpie.say("чем"),
        npc.Owl.say("Двухфакторной аутентификации нет ни у кого."),
        npc.Squirrel.say("Ну вы даете"),
        npc.Owl.info("Двухфакторная аутентификация - это алгоритм идентификации пользователя, для выполнения которого пользователю нужно предъявить несколько (в нашем случае 2) доказательств, подтверждающих, что вы - это вы."),
        npc.Owl.info("Например, если кто-то узнал ваш пароль от почты, но при этом у вас стояла двухфакторка, то этому кому-то понадобится второй фактор (обычно это смартфон, который связан с этой почтой), чтобы заполучить ваши данные."),
        npc.Owl.info("К сожалению, смс-оповещения не самая безопасная вещь, поэтому вы можете установить на свои телефоны OTP Auth для iOS и andOTP для android - они сами связываются с сервисами и генерируют коды подтверждения."),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Floppa.say("Ха, то есть мой телефон - это золотой ключик?) А если его заберёт себе какая-нибудь черепаха? Как я тогда попаду в свой театр???"),
        npc.Owl.say("Для этого вам нужно позаботиться ещё об одном моменте - **резервных кодах**. Резервные коды это целый список ваших личных кодов, созданный вашим сервисом или программой для генерации кодов, как раз на тот случай, если у вас нет доступа телефону."),
        npc.Owl.say("У всех вас наверняка есть аккаунты в гугле! Если у вас нет двухфакторки там, то обязательно установите. А потом скачайте свои резервные коды оттуда, но помните, что каждый из них работает только один раз."),
        npc.Squirrel.say("Напишите мне готово, когда закончите!"),
        npc.Floppa.say("Слушайте"),
        npc.Floppa.say("А если в сервисе, которым я пользуюсь, нет двухфакторки? Что тогда делать?"),
        npc.Magpie.say("тогда, наверное, не стоит им пользоваться"),
        npc.Floppa.say("Но ведь там скидки на квас..."),
        npc.Magpie.say("кому нужны твои скидки"),
        npc.Owl.say("Спокойно! Никто не потеряет никаких скидок."),
        npc.Owl.say("Но Флоппа правильно сказал, что есть сервисы без двухфакторки. ****Теперь вам нужно заменить все ваши пароли на более сложные."),
        npc.Floppa.say("Пароль yalublukvas достаточно сложный?"),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("Не очень. Зная тебя, даже Сорока сможет его подобрать. Попробуй лучше ja04[#lublu@kvas4](https://vk.com/im?sel=60840357&st=%23lublu%40kvas4)"),
        npc.Floppa.say("Не понимаю, а какая разница?"),
        npc.Owl.say("К сожалению, разница есть. Пароль, который ты предложил, простой, потому что он плоностью состоит из слов. Кроме того, в нём не хватает цифр и специальных символов."),
        npc.Owl.say("В действительно сложных паролях обязательно присутствуют спецсимволы, цифры и в них, как правило, нет слов."),
        npc.Magpie.say("сложного и так каждый день по горло, так ещё и с паролем заморачиваться"),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("Тогда можешь воспользоваться **генераторами паролей**. Сейчас их очень много, но лучше использовать те, которые точно не сохраняют ваши пароли на своих сервисах, например, [https://www.random.org/passwords/](https://www.random.org/passwords/) или специальную программу KeePass."),
        npc.Owl.say("Есть ещё одно важное правило: нельзя ставить один и тот же пароль, каким бы сложным он ни был, на несколько сайтов. И забудьте про автозаполнение!"),
        npc.Floppa.say("А как я запомню-то их все? Обвесить мой ноутбук стикерами с паролями звучит не очень безопасно..."),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("Запоминать ничего не нужно, для этого есть менеджеры паролей. Например, тот же самый KeePass. Эта программа мультиплатформная, вы можете поставить их на любые устройства с любой оперативной системой. Посмотрите, как много у нее вариантов! [https://keepass.info/download.html](https://keepass.info/download.html) - тут и для айфона, и для айпада есть!"),
        npc.Squirrel.say("Ну это всё личные, а с корпоративными аккаунтами что?"),
        npc.Magpie.say("да! если с кем-то из нас что-то случится у редакции должен остаться доступ к его данным"),
        npc.Owl.info("Есть и такие менеджеры! Большинство из них позволяет надёжно хранить пароли сразу нескольким пользователям как раз для таких случаев. Вот в как раз в KeePass можно не только держать свои пароли, но и добавлять пароли других пользователей. Главное, что эта программа имеет открытый код и послностью бесплатна для вас!"),

        npc.Floppa.say("Ура!!! Теперь мы защищены до зубов!!"),
        npc.Magpie.say("так никто не говорит.... вооружены до зубов а не защищены"),
        npc.Squirrel.say("Сорока! А давай узнаем о случаях взлома у разных медиа и активистов"),
        npc.Magpie.say("всё перестаю щёлкать клювом в чате и вылетаю"),
        npc.Floppa.say("Удачи!"),
        Proceed(threat = True)
    ],

    threat = [
        npc.Magpie.say("блин"),
        npc.Magpie.say("эти придурки поджигатели распугали моих респондентов"),
        npc.Magpie.say("посмотрите"),
        npc.Magpie.say("**Текст поста из тг канала Чистый лес**"),
        npc.Magpie.say("они правда нашли адреса?"),
        npc.Owl.say("Возможно. Как я и говорил, найти личные данные любого пользователя проще, чем кажется. Пара фотографий, общие друзья, один лайк под постом и всё, вас сцапали."),
        npc.Floppa.say("рррррр"),
        npc.Magpie.say("ну а я-то тут причем"),
        npc.Magpie.say("как мне доказать что со мной можно безопасно разговаривать??"),
        npc.Owl.say("В телеграме для этого есть несколько важных функций."),
        npc.Owl.info("Первое - это *сикрет-чаты.* В них информация не хранится на серверах, а пересылается между собеседниками лично, в них используется сквозное шифрование. **В таких чатах есть *удаление сообщений по таймеру*. "),
        npc.Owl.say("Сейчас во всех чатах можно настроить автоудаление, никогда не забывайте об этом."),
        npc.Floppa.say("Только тут ничего не удаляйте, пожалуйста...."),
        npc.Owl.info("В телеграме можно не показывать свой номер никому, кроме тех, у кого он уже записан, а вот Signal позволяет использовать вообще любой номер телефона, делая общение практически анонимным для третьих лиц, и в нём есть все те же функции: от автоудаления до сквозного шифрования. Кроме того, у него полностью открытый код, и мы точно знаем, как именно он работет. Например, он точно-точно не собирает метаданные!"),
        npc.Owl.info("Ещё есть такая штука, как Delta Chat! Она полностью децентрализована, а чтобы ей пользоваться нужна всего лишь электронная почта! Более того, твои сообщения дойдут даже в том случае, если у адресата не стоит Delta Chat"),
        npc.Magpie.say("хмм неплохо"),
        npc.Magpie.say("надеюсь это поможет"),
        npc.Owl.say("Погоди! Если тебе попадётся уж очень пугливый источник, то тогда тебе на помощь придёт Wire - это мессенджер, в котором тоже есть автоудаление и другие полезные функции, но в нём вообще всё защищено сквозным шифрованием, вплоть до видеозвонков."),
        npc.Magpie.say("кажется мне понадобится помощь"),
        npc.Magpie.say("Сова, ты полетишь со мной?"),
        npc.Owl.say("Конечно! "),
        npc.Squirrel.say("Удачи вам!"),
        npc.Squirrel.say("Новенькие, можете отдохнуть сейчас"),
        npc.Squirrel.say("Или скрыть свои номера телефонов, например!"),
        #В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("""Прямо сейчас у вас есть возможность зайти в настройки телеграма и изменить настройки приватности. Самое важное что вы можете сделать:
+ Скрыть свой номер телефона
+ Отключить p2p звонки
+ Отключить доступ к вашему профилю через пересланные сообщения   
"""),
        npc.Squirrel.say("Слушайте, перед Совой было стыдно, можно сейчас признаюсь"),
        npc.Squirrel.say("Мне очень жаль, что мы начали думать о безопасности только сейчас, когда у нас и наших друзей неприятности"),
        npc.Squirrel.say("Мне кажется, я сегодня всех сильно подставила"),
        npc.Floppa.say("Эй"),
        npc.Floppa.say("Ну камон"),
        npc.Floppa.say("Ну откуда ты могла знать, что в соседней норе живут звери, которые будут себя так гадко вести? Всего не предугадаешь"),
        npc.Floppa.say("Вы сегодня смогли защитить друг друга и прекрасного меня! И больше с вами никаких ужасов не случится! РРРРР"),
        npc.Floppa.say("Так что давайте наконец-то хоть немного расслабимс"),
        npc.Squirrel.ask("Да, отличный момент чтобы сделать небольшой перерыв! Приступайте, когда почувствуете что есть силы продолжать игру.", [("Продолжить", "next")], Var.null),
        Proceed(final = True)
    ],

    final = [
        npc.Magpie.say("поздравьте нас"),
        npc.Owl.say("Это ужасно глупая история"),
        npc.Magpie.say(docs['investigation']),
        npc.Squirrel.say("Вау, тут вообще ничего не надо редактировать"),
        npc.Floppa.say("У меня аж кисточки на ушах затряслись..."),
        npc.Squirrel.ask("Ну что, публикуем?", [("Опубликовать", "next")], Var.null),
        score.add(5),
        npc.Squirrel.say("Вы все молодцы! Я очень нами горжусь"),
        npc.Floppa.say("Теперь можно налить себе кружечку кваса и вытянуться на диване"),
        npc.Floppa.say("Подождите!!! А что со взломщиками??? Вы их нашли???????"),
        npc.Owl.say("Никак нет"),
        npc.Owl.say("Этим уже занимается полиция"),
        npc.Squirrel.say("Значит, мы можем быть спокойны"),
        npc.Squirrel.say("КОНЕЦ ПЕРВОГО МОДУЛЯ")
    ]
)
