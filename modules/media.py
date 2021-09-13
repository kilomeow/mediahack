from engine.glide import StoryMap
from engine.var import Var, Proceed, Jump

from modules.init import npc, score, docs

description = "Социальные сети и мессенджеры"

content = StoryMap(
    entry=[
        npc.Squirrel.say("Сорока, вы там готовы?"),
        npc.Magpie.say("почти закончили"),
        npc.Floppa.say("Урааа"),
        npc.Floppa.say("Это ведь материалы про лагерь погорельцев, в котором работает Кролик, да??"),
        npc.Rabbit.say("Так точно"),
        npc.Rabbit.say("Мы ещё на месте"),
        npc.Floppa.say("Как там сейчас?"),
        npc.Rabbit.say("Если честно, то очень тяжело"),
        npc.Rabbit.say("Здесь очень много пострадавших, и у нас проблемы с водой"),
        npc.Floppa.say("Жеесть, сил вам!!"),
        npc.Rabbit.say("Спасибо!"),
        npc.Squirrel.say("ВНИМАНИЕ"),
        #М: НЕ ДО КОНЦА ПОНИМАЮ, ОТКУДА ПО СЮЖЕТУ ВЗЯЛСЯ ЭТОТ ДОКУМЕНТ. ЭТО СОРОКА ПРИСЛАЛА? ПОЧЕМУ ТОГДА НЕ ЧЕРЕЗ ЧАТИК?
        npc.Squirrel.say(
            "Жду редактуру! Нужно сделать источники анонимными (Наш дом это НЕ анонимная организация, мы про них и пишем, если что, можете считать это партнёрским материалом), если они есть, и убрать авторские примечания "
            "в скобках"),
        npc.Squirrel.say(docs['note1']),
        npc.Floppa.say("Да! И не забывайте советоваться друг с другом в чятике"),
        npc.Floppa.say("Командная работа это не пельмени варить"),
        npc.Floppa.say("Хотя..."),
        npc.Squirrel.say("Мне сейчас срочно надо развесить грибы сушиться"),
        npc.Squirrel.ask("Нажмите «Готово», когда закончите, и я тут же вернусь", [("Готово", "ready")], Var.null),

        score.add(3),

        npc.Magpie.say("нам тут прислали кое-что"),
        npc.Floppa.say("Что?"),
        npc.Magpie.say("кое-что неприятное"),
        npc.Magpie.say("не уверена, что новеньким стоит это читать"),
        npc.Floppa.say("Там что-то жуткое?"),
        npc.Magpie.say("мне бы не хотелось вас вот так сходу шокировать"),
        npc.Floppa.say("Да что там"),
        npc.Magpie.say("ладно, ща пришлю"),
        npc.Magpie.say("только не пугайтесь особо"), [("Посмотреть", "ready")], Var.null),
        npc.Magpie.info("""Вы хотели привлечь внимание и вы его привлекли. Не все здесь хотят видеть немытых""" +
                        """мигрантов у себя под окнами. Скажите вашим пушистым друзьям, чтобы сворачивали свои""" +
                        """палатки и шли в другое 
место, пока мы их не нашли. Мы не хотим кормить их за свой счет. Как и вашу газетёнку. 

Прекращайте этот балаган немедленно. """),
        npc.Rabbit.say("Вот об этом я и говорил"),
        npc.Squirrel.say("И что нам теперь делать"),
        npc.Rabbit.say("Ну я пока ничего страшного не вижу"),
        npc.Rabbit.say("Чем больше зверей узнают о Сорокином хвосте, тем лучше"),
        npc.Magpie.say("зверей и птиц, прошу заметить"),
        npc.Rabbit.say("Короче, не важно, че там кто пишет"),
        npc.Rabbit.say("Давайте следующую заметку тогда"),
        #М: ЧТО ЗНАЧИТ «ДАВАЙТЕ СЛЕДУЮЩУЮ ЗАМЕТКУ»? ДАВАЙТЕ ОПУБЛИКУЕМ? 
        npc.Rabbit.say(docs["note2"]),  # вот он тут, я не знаю, почему его нет в игре
        npc.Rabbit.say(
            "Вот этот текст вычитайте прям очень внимательно, пожалуйста, я торопился и мог что-то проглядеть"),
        npc.Squirrel.say("Ок! "),
        npc.Squirrel.say("Ребята-зверята, Кролик не убрал пару примечаний за собой. Найдите их и уберите, пожалуйста."),
        #М: А ЕСЛИ КОНКРЕТНЕЕ, ЧТО ОНИ ДОЛЖНЫ УБРАТЬ ИЗ ЭТОГО ДОКУМЕНТА? КАКИЕ СЛОВА?
        npc.Squirrel.ask('Закончили?', [("Готово", "ready")], Var.null),

        score.add(3),
        npc.Magpie.say(".........."),
        npc.Magpie.say("они не унимаются"),
        npc.Magpie.say("видимо, нас читают бескультурные звери, которым нечем заняться "),
        npc.Magpie.say("нам снова пришла порция гадостей"),
        npc.Magpie.say("теперь тут прямо лично про меня"),
        npc.Magpie.ask("очень мерзко", [("Посмотреть", "ready")], Var.null),
        npc.Magpie.info("""```Привет, Сорока! Я уже купил спички и собираюсь устроить пикник недалеко от леса! Скажи ты 
любишь загорать? Если да то тебе понравится гореть будет очень ярко! А потом я обязательно зайду к вам в 
гости я слышал что вы любите всякие горячие новости а будет очень горячо.... 

З.Ы. Передавай обгоревшим уродам привет```"""),
        npc.Rabbit.say("Забей"),
        npc.Rabbit.say("Какой-то третьеклассник написал"),
        npc.Floppa.say("Буквы в интернете ещё никого не убивали"),
        npc.Magpie.say("это да, но всё равно стрёмно"),
        npc.Magpie.say("кто знает, что в голове у этих типов"),
        npc.Floppa.say("Мне кажется, к этому нужно просто привыкнуть...."),
        #ТУТ БЫЛА ИСПОВЕДЬ СОРОКИ, НО ОНА НИКАК НЕ ПОМОГАЕТ СЮЖЕТУ, ПОЭТОМУ ПРЕДЛОЖИЛА БЫ СОКРАТИТЬ
        npc.Floppa.say("Они хотят запугать тебя, чтобы ты ничего не писала"),
        npc.Floppa.say("Нужно сжать клюв и продолжать делать правильные вещи!"),
        Proceed(photo=True)
    ],

    photo=[
        npc.Rabbit.info("А вот сейчас я реально напрягся"),
        npc.Rabbit.say("Выложил в инсту фотку из лагеря, и в комменты набежали какие-то типы"),
        npc.Rabbit.say("Никогда не видел столько хейта"),
        npc.Rabbit.say("Пишут, что хотят всё сжечь"),
        npc.Floppa.say("Посмотри на юзернеймы, наверняка боты"),
        npc.Floppa.say("Да даже если живые звери, такие только вякать и умеют "),
        npc.Floppa.say("А сами сидят на диване ровно "),
        npc.Magpie.say("зачем ты вообще это выложил??? "),
        npc.Magpie.say("разве не ты просил меня не писать, где лагерь??"),
        npc.Floppa.say("Да всё нормально! Вряд ли вас кто-то вычислит по веткам))"),
        npc.Magpie.say("уже"),
        npc.Magpie.say("смотри, что пишут в телеграм-канале Чистый Лес"),
        npc.Magpie.info(""" ```Мы уже оперативно вычислили всех, кто сочувствует облезлому Сорокиному хвосту. Их имена и 
адреса установлены. Настоятельно рекомендуем всем, 
кто хочет открыть свою пасть, немедленно захлопнуть её ради своей же безопасности.```"""),
        npc.Floppa.say("Это ваще кто??"),
        npc.Rabbit.say("Пусть только попробуют с кем-то лично связаться, я им блин хвосты повыдёргиваю"),
        npc.Magpie.say("это короче наши дорогие ретарды"),
        npc.Rabbit.say("Раз на раз без маек на траве"),
        npc.Magpie.say("они уже давно топят за Хвойный лес для хвойнослесных "),
        npc.Magpie.say("только странно, раньше они подобным не промышляли"),
        npc.Squirrel.say("Спокойно"),
        npc.Squirrel.say("Как они вообще нас вычислили???"),
        npc.Squirrel.say("Сова, что теперь делать?"),
        npc.Owl.say(
            "Кролику не стоило выкладывать эту фотографию в общий доступ. Сейчас довольно легко установить, "
            "конкретное место на фотографии. Например, по виду из окна. Или по строению на фоне, "
            "это может быть что угодно."),
        npc.Rabbit.say("Блин, я только что понял),
        npc.Rabbit.say("На фотку попал старый дуб"),
        npc.Rabbit.say("Его реально все в лесу знают"),
        npc.Rabbit.say("Как я мог так факапнуться...."),
        npc.Rabbit.say("Капец"),
        npc.Owl.say(
            "Кролик, бери лапы в лапы и беги к нотариусу. Тебе нужен *«Акт осмотра страницы в сети «Интернет»* двух "
            "этих скриншотов с угрозами*.* Жалобу в Telegram я уже отправила, хотя это может ни на что не повлиять."),
        npc.Owl.say(
            "Можно было бы ещё обратиться в полицию, но я не уверена, что они будут что-то предпринимать. Будем "
            "действовать по ситуации"),
        npc.Rabbit.say("Мне сейчас реально нужно бежать к нотариусу???"),
        npc.Owl.say("ДА."),
        npc.Squirrel.say("Да!"),
        npc.Rabbit.say("Ладно ладно"),
        npc.Rabbit.say("Побежал"),
        npc.Squirrel.say("А нам что делать? Тут и про нас есть!"),
        npc.Owl.say("Тут нужно подумать."),
        npc.Owl.say(
            "Вы  можете сообщить об угрозах читателям, это точно привлечет внимание. С другой стороны, "
            "так можно спровоцировать недоброжелателей."),
        npc.Magpie.say("хммм"),
        npc.Floppa.say("Как это в шахматах назвается??"),
        npc.Floppa.say("Точно, вилка!"),
        npc.Squirrel.say("Нужно подумать, это очень серьёзная ситуация. Давайте проголосуем."),
        npc.Squirrel.ask("Выбор за вами!", [("Сообщаем", "public"), ("Не сообщаем", "not_public")],
                         Var.threat_public),
        Jump(Var.threat_public)
    ],
    # ЗДЕСЬ———————игроки голосуют———————

    # ПОСЛЕДСТВИЯ: Сообщаем

    public=[
        npc.Squirrel.say("Что ж, решено"),
        npc.Magpie.say("хорошо! я сейчас подготовлю и выкачу пост"),
        score.add(2),
        npc.Squirrel.say("У поста очень много просмотров! Наверное, это хорошо..."),
        npc.Floppa.say("Вы молодцы!"),
        npc.Magpie.say("нам приходит очень много слов поддержки"),
        npc.Magpie.say("мне даже как-то легче стало"),
        npc.Squirrel.say("Это же прекрасно!"),
        npc.Squirrel.say("Всем спасибо, работаем дальше"),
        Proceed(threat=True)
    ],

    not_public=[
        npc.Squirrel.say("Ладно, будем просто следить за ситуацией"),
        npc.Floppa.say("И правильно! Не будем кормить троллей"),
        npc.Floppa.say("Кролик напишет заявление, и пусть полиция с ними говорит"),
        npc.Magpie.say("если заявление вообще примут"),
        npc.Squirrel.say("В любом случае, работаем дальше"),
        Proceed(threat=True)
    ],
    threat=[
        npc.Magpie.say("блин"),
        npc.Magpie.say("эти придурки поджигатели распугали моих респондентов"),
        npc.Magpie.say("посмотрите"),
    #М: ТУТ ПОЧЕМУ-ТО ПОВТОРЯЕТСЯ ТЕКСТ УГРОЗЫ СО СТРОКИ 99, НУЖНА ДРУГАЯ, НАВЕРНОЕ? 
        npc.Magpie.say("```Мы уже оперативно вычислили всех, кто сочувствует облезлому Сорокиному хвосту. Их имена и "
                       "адреса установлены, их любимая газетёнка даже не думала их спасать.```"
                       "```Мы настоятельно рекомендуем всем, кто хочет открыть свою пасть, немедленно её захлопнуть ради "
                       "своей же безопасности.```"),
        npc.Magpie.say("они правда нашли адреса??"),
        npc.Owl.say(
            "Возможно. Как я и говорила, найти личные данные любого пользователя проще, чем кажется. Пара фотографий, "
            "общие друзья, лайк под определённым постом, и всё — вы под колпаком."),
        npc.Floppa.say("Рррррр"),
        npc.Magpie.say("ну а я-то тут при чем?? "),
        npc.Magpie.say("как мне доказать, что со мной можно безопасно разговаривать?"),
        npc.Owl.say("Есть пара идей."),
        npc.Owl.info(
            "Во-первых, ты можешь предложить им пообщаться в секретном чате в Telegram. В этом случае вся ваша переписка "
            "будет защищена сквозным шифрованием. Даже если кому-то удастся её перехватить, он увидит бессмысленный "
            "набор символов. А ещё секретные сообщения, в отличие от обычных, передаются напрямую от собеседника к "
            "собеседнику и минуют сервер Telegram. Их не сможет прочитать даже Павел Дуров! "),
        npc.Owl.say("Скринить или пересылать секретные сообщения тоже нельзя — всё останется только между тобой и информатором. "
        npc.Owl.say("А для максимальной безопасности ещё можно поставить таймер автоудаления сообщений. Чтобы "
            "они исчезали без следа, скажем, через минуту после прочтения. "),
        npc.Floppa.say("Как говорится, после прочтения сжечь...."),
        npc.Magpie.say("звучит прикольно "),
        npc.Magpie.say("а как начать этот секретный чат? "),
        npc.Owl.say("Нажми на аватарку собеседника, а потом — на многоточие в правой части экрана. Выбери «Начать секретный чат». "),
        npc.Magpie.say("чет не нахожу такого с ноута "),
        npc.Owl.say("А это потому, что секретные чаты есть только в мобильной версии Telegram. "),
        npc.Magpie.say("вот блин, я с ноута обычно общаюсь ")
        npc.Owl.info(
            "Тогда обрати внимание на ```Signal``` и ```Wire```. В этих мессенджерах абсолютно все чаты защищены "
            "сквозным шифрованием — а не только секретные, как в Telegram. Звонки по аудио и видео тоже идут мимо "
            "сервера, их нельзя перехватить. А ещё у этих мессенджеров открытый код — любой желающий может убедиться, "
            "что они не собирают и не хранят данные о пользователях, в отличие от того же Telegram "),
        npc.Magpie.say("ух ты "),
        npc.Magpie.say("но блин, телега есть у всех "),
        npc.Magpie.say("а про сигнал и вайр я впервые слышу, уверена, что многие тоже "),
        npc.Magpie.say("не каждый будет готов что-то там инсталлить ради разговора со мной "),
        npc.Owl.say("Тогда тебе на помощь придёт Delta Chat. "),
        npc.Owl.info(
            "```Delta Chat``` – это мессенджер, который привязан не к телефону, а к электронной почте. "
            "С его помощью можешь общаться даже с теми, у кого не стоит Delta Chat — твой собеседник "
            "будет получать от тебя обычный e-mail и отвечать на него, как на обычный e-mail. Вот только "
            "благодаря Delta Chat ваша переписка будет защищена сквозным шифрованием и никто не сможет "
            "получить к ней доступ, кроме вас двоих. "),
        npc.Magpie.say("хмм звучит неплохо"),
        npc.Magpie.say("надеюсь это поможет"),
        npc.Floppa.say("День удивительных открытий...."),
        npc.Squirrel.say("Было бы круто найти зверей и птиц, которым угрожали из-за сотрудничества с Нашим домом"),
        npc.Squirrel.say("Когда начались пожары, у них было достаточно много волонтёров, которые потом ушли"),
        #М: ТУТ НЕ ДО КОНЦА ПОНИМАЮ, ЧТО ЗНАЧИТ «КОТОРЫЕ ПОТОМ УШЛИ». УШЛИ = ПЕРЕСТАЛИ СОТРУДНИЧАТЬ?
        npc.Magpie.say("кажется мне понадобится помощь"),
        npc.Magpie.say("Сова, полетишь со мной?"),
        npc.Owl.say("Конечно! "),
        npc.Squirrel.say("Удачи вам!"),
        npc.Squirrel.say("Новенькие, если вы утомились, можете сделать перерыв сейчас"),
        # М: А ПОЧЕМУ БЕЛКА ПРЕДЛАГАЕТ СДЕЛАТЬ ПЕРЕРЫВ И ТУТ, И В СТРОКЕ 263? 
        npc.Squirrel.say("Или воспользоваться моментом и изменить настройки Telegram, чтобы защитить свои данные!"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Squirrel.info("""Чтобы обезопасить себя при общении в обычных чатах, зайдите в Настройки — Конфиденциальность и:
+ Скройте ваш номер телефона (Номер телефона — Кто видит мой номер телефона? — Никто, Кто может найти меня по номеру? — Мои контакты)
+ Отключить p2p звонки (Звонки — Peer-to-peer — «Никогда»)
+ Отключить доступ к вашему профилю через пересланные сообщения (Пересылка сообщений — Кто может ссылаться на мой аккаунт при пересылке сообщений? — Никто)
"""),
        # ИЛИ МОЖНО ВМЕСТО ИНСТРУКЦИИ ПРИСЛАТЬ ГИФКУ С ДЕЙСТВИЯМИ, ЧТОБЫ БЫЛО ВИДНО, КУДА НАЖИМАТЬ
        npc.Squirrel.say("Слушайте, можно признаюсь? Перед Совой было стыдно сейчас "),
        #М: А ПОЧЕМУ БЕЛКА СЧИТАЕТ, ЧТО ОНА ВСЕХ ПОДСТАВИЛА? ОНА ВРОДЕ КАК НИЧЕГО НЕ ДЕЛАЛА, В ОТЛИЧИЕ ОТ ТОГО ЖЕ КРОЛИКА            
        npc.Squirrel.say(
            "Мне очень жаль, что мы начали думать о безопасности только сейчас, когда у нас и наших друзей"
            " неприятности"),
        npc.Squirrel.say("Мне кажется, я сегодня всех сильно подставила"),
        npc.Floppa.say("Эй"),
        npc.Floppa.say("Ну камон"),
        npc.Floppa.say(
            "Ну откуда ты могла знать, что в соседней норе живут звери, которые будут себя так гадко вести? Всего не "
            "предугадаешь"),
        npc.Floppa.say(
            "Сегодня вы узнали, как защитить друг друга и прекрасного меня! Никаких ужасов с нами не случится! "
            "РРРРР"),
        npc.Floppa.say("Так что давайте наконец-то хоть немного расслабимся"),
      
        Proceed(game_break=True)
    ],

    game_break=[
        npc.Squirrel.ask(
            "Ребята, вы очень хорошо потрудились. Предложу вам чуть-чуть отдохнуть, заварить себе чай."
            "Возвращайтесь, когда почувствуете, что у вас есть силы продолжить игру.",
            [("Отдохнули", "relax")], Var.null),
        # Proceed(vzlom=True)
        # М: ТУТ БЫ ЕЩЁ СОСЛАТЬСЯ НА ВРЕМЕННЫЕ ОТСЕЧКИ: МОЛ, ВЫ ПРОШЛИ ТРЕТЬ ИЛИ ПОЛОВИНУ ИГРЫ, ВПЕРЕДИ ЕЩЁ ПОЛЧАСА ПРИМЕРНО. ПРЕДЛОЖУ, КОГДА СМОГУ ВСЁ ПОТЕСТИРОВАТЬ И ЗАСЕЧЬ
    ]
)
