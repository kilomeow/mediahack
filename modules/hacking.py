from engine.glide import StoryMap
from engine.var import Var, Jump, Proceed

from modules.init import npc

description = "Взлом"

content = StoryMap(
    entry=[
        npc.Squirrel.say("Сорока, ты не знаешь, где сейчас Кролик?"),
        npc.Magpie.say("что случилось?"),
        npc.Squirrel.say("Он должен был прислать мне инфографику по беженцам "),
        npc.Magpie.say("сейчас наберу его"),
        npc.Magpie.say("не отвечает"),
        npc.Floppa.say("Может, занят?"),
        npc.Magpie.say("он в сети был 10 часов назад"),
        npc.Magpie.say("а ушастый жить не может без уютных чатов с картинками"),
        npc.Floppa.say("Понимаю его... Тогда это реально странно"),
        npc.Floppa.say("Мб он уснул просто"),
        npc.Squirrel.say("У меня вроде ничего не горит, но я так много волноваться начала в последнее время"),
        npc.Floppa.say("Тебе просто нужно отдохнуть!"),
        npc.Squirrel.say("Может, это было бы и неплохо"),
        npc.Squirrel.say("Но если я буду отдыхать, то буду волноваться не из-за работы, а из-за того, что я не работаю("),
        npc.Magpie.say(":))))))))))))))))))))))))))))))) так же себя чувствую"),
        npc.Rabbit.say("Здравствуйте, коллеги!"),
        npc.Rabbit.say(
            "С прискорбием сообщаю от лица нашей организации о закрытии лагеря. Эти животные совершенно не хотят жить "
            "по правилам, поэтому мы вынуждены прекратить нашу деятельность."),
        npc.Floppa.say("Чегоо???"),
        npc.Squirrel.say("Эээ."),
        npc.Rabbit.say(
            "Мы просим удалить вас все материалы о нашей организации и лагере. Мы знаем, что это противоречит вашей "
            "политике, но мы действительно хотели бы полностью забыть эту историю."),
        npc.Floppa.say("А что с беженцами?"),
        npc.Rabbit.say("Мы перенаправим их в другие убежища. "),
        npc.Squirrel.say(
            "Мы не можем удалять материалы, но мы можем опубликовать ваш комментарий по поводу закрытия шелтера."),
        npc.Floppa.say("Что у вас случилось??????"),
        npc.Rabbit.say(
            "Мы дадим комментарий только в обмен на удаление материалов. К сожалению, никак иначе мы не можем, "
            "это нужно в целях безопасности."),
        npc.Floppa.say("Кролик?"),
        npc.Floppa.say("Мне это не нравится"),
        npc.Floppa.say("Белка, это очень странно. Кролика могли взломать?"),
        npc.Squirrel.say("Не знаю"),
        npc.Magpie.say("это реально какой-то очень странный прикол"),
        npc.Magpie.say("кроль, мб ты объяснишься? ниче не хочешь мне сказать???"),
        npc.Magpie.say("там вообще то куча моей работы, и твоей тоже"),
        npc.Floppa.say("Сорока, не наезжай сейчас ни на кого, пожалуйста, побереги нервы"),
        npc.Magpie.say("ушастый не берёт трубку"),
        npc.Magpie.say("класс"),
        npc.Squirrel.say("Так его реально взломали?"),
        npc.Squirrel.say("Мне бы не хотелось, чтобы наша переписка оказалась в чьих-то лапах..."),
        npc.Squirrel.say("Давайте проголосуем! Если вы считаете, что Кролик взломан, я удалю его из чата"),
        # В СТРОКЕ НИЖЕ ДОЛЖНО БЫТЬ ГОЛОСОВАНИЕ
        npc.Squirrel.ask("Кролик взломан?", [("Взломан", "hacked"), ("Не взломан", "not_hacked")], Var.rabbit_hacked),
        Jump(Var.rabbit_hacked)
        # ЗДЕСЬ     ****———————игроки голосуют———————
    ],

    hacked=[
        #    - **ПОСЛЕДСТВИЯ: Кролик взломан!**

        npc.Squirrel.say("***удаляет Кролика из чата***"),
        npc.Squirrel.say("Надеюсь, мы поступили правильно."),
        Proceed(password=True)
    ],

    not_hacked=[
        #    - **ПОСЛЕДСТВИЯ: Кролик не взломан!**

        npc.Squirrel.say("Ладно, Кролик."),
        npc.Squirrel.say("Сейчас я уберу с сайта заметки."),
        npc.Squirrel.say("**шкала злободневности -**"),
        npc.Squirrel.say("..."),
        npc.Squirrel.say("Мне только что позвонили из Нашего Дома"),
        npc.Squirrel.say("Кролика всё-таки взломали..."),
        npc.Squirrel.say("***удаляет Кролика из чата***"),
        npc.Floppa.say("Ты же можешь вернуть материалы?"),
        npc.Squirrel.say("Конечно, сейчас"),
        npc.Squirrel.say("Блин, ситуация отстой"),
        npc.Floppa.say("Ничего страшного, ты просто никогда с таким не сталкивались!"),
        npc.Floppa.say("И ты ведь смогла всё исправить"), 
        Proceed(password=True)
    ],
    
    password=[
        npc.Magpie.say("смотрите, что выкатил наш дом"),
        npc.Magpie.say(
            "```Привет, это зайчиха Варвара. Мы потеряли связь с нашим сотрудником кроликом Степаном.  Пожалуйста, ```"
            "```сообщите нам, если вам что-либо известно.\nUPD: В телеграм-аккаунты трех наших сотрудников пытались ```"
            "```войти. ```"),
        npc.Magpie.say("жуть какая-то"),
        npc.Floppa.say("У вас раньше уже было что-то подобное? Это похоже на массовый взлом???"),
        npc.Floppa.say("Зачем они пытаются кого-то взламывать??????"),
        npc.Squirrel.say("Я одна не понимаю, на что они надеются?"),
        npc.Squirrel.say("Ведь чтобы зайти в Telegram с нового устройства, нужен смс-код"),
        npc.Squirrel.say("Они же не могут его получить... Или как?"),
        npc.Owl.say("Ну вообще могут."),
        npc.Owl.say("SMS-сообщения можно перехватить."),
        npc.Owl.say("Именно поэтому рекомендую всем настроить двухфакторную аутентификацию."),
        npc.Owl.say(
            "Если у вас стоит двухфакторная аутентификация, то для запуска вашего Telegram на "
            "другом устройстве понадобится не только SMS-код, но и специальный пароль, который "
            "знаете только вы. "),
        npc.Owl.info(
            "Чтобы установить двухфакторку, перейдите в Настройки — Конфиденциальность — Облачный пароль. "
            "После ввода пароля вас попросят придумать подсказку к нему и указать электронную почту, куда "
            "придёт проверочный код для подтверждения пароля. Введите его в соответствующее поле — вуаля, "
            "двухфакторка установлена "),
        npc.Squirrel.say("Надо попробовать"),
        npc.Squirrel.say("А двухфакторка есть только в Телеграме?"),
        npc.Owl.say("Её можно подключить для большинства сервисов и соцсетей — Instagram, Facebook, Gmail. "),
        npc.Owl.say("В этом случае всё будет наоборот: так как обычно вы входите туда с помощью пароля, сервис
                    "попросит вас привязать аккаунт к телефону на случай взлома "),
        npc.Floppa.say("Но ты же только что сказала, что смски небезопасны...."),
        npc.Owl.say("Флоппа, позволь мне закончить. :)"),
        npc.Owl.say("Так как SMS-сообщения можно перехватить, рекомендую вам установить на телефоны приложения "
                    "'''OTP '''Auth''' для iOS и '''andOTP''' для Android. Когда вы привяжете свои аккаунты к этим "
                    "приложениям, секретные коды будут приходить не в виде SMS, а в виде пуш-уведомлений — "
                    "то есть, прямо в эти приложения. Пуш-уведомления перехватить невозможно. "),
        npc.Floppa.say(
            "Ха, то есть мой телефон - это золотой ключик?) А если его заберёт какая-нибудь черепаха? Как я "
            "тогда попаду в свой театр???"),
        npc.Owl.say(
            "Для этого вам нужно позаботиться о **резервных кодах**. Резервный код "
            "можно ввести вместо секретного кода. Это пригодится, если у вас нет доступа к телефону."),
        npc.Owl.say(
            "Выглядят резервные коды примерно так: "),
         #М: В СООБЩЕНИЕ СОВЫ ВСТАВИТЬ БЫ КАКОЙ-ТО СКРИН, КОТОРЫЙ ПОКАЖЕТ, КАК ВЫГЛЯДЯТ РЕЗЕРВНЫЕ КОДЫ, НАПРИМЕР: https://help.mail.ru/pic/4/6/4699cf9690329de953b0df51ff64c63a.png
        npc.Magpie.say("а если их кто-то увидит у меня в гнезде или заберёт??"),
        npc.Owl.say(
            "Их несколько, и каждый из них работает только один раз. Поэтому лучше всего распечатать этот"
            "список или где-то записать. "),
        npc.Magpie.say("а их безопасно вот так просто хранить? "),
        npc.Magpie.say("если их кто-то увидит у меня в гнезде и заберёт??"),
        npc.Owl.say(
            "Никто, кроме тебя, не знает, что это за наборы цифр и что с ними делать. "
            "Запомнить все коды невозможно, поэтому лучше так. "),
        npc.Owl.say("Давайте потренируемся на примере аккаунтов в Google — они наверняка есть у всех. Установите "
                    "себе двухфакторную аутентификацию, а потом скачайте и распечатайте свои резервные коды. "),
        npc.Owl.say("Переходите по ссылке и следуйте инструкциям, это займёт 5 минут: [https://www.google.com/landing/2step/?hl=ru]("
            "https://www.google.com/landing/2step/?hl=ru)"),
        npc.Squirrel.say("Пожалуйста, нажмите кнопку ниже, когда закончите!"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("**[Установили двухфакторную аутентификацию]**"),
        npc.Squirrel.say("Прекрасно!"),
        npc.Floppa.say("Слушайте"),
        npc.Floppa.say("А если в сервисе, которым я пользуюсь, нет двухфакторки? Что тогда делать?"),
        npc.Magpie.say("тогда, наверное, не стоит им пользоваться"),
        npc.Floppa.say("Но ведь там скидки на квас..."),
        npc.Magpie.say("кому нужны твои скидки"),
        npc.Owl.say("Спокойно! Никто не потеряет никаких скидок."),
        npc.Owl.say(
            "Но Флоппа правильно сказал, что есть сервисы без двухфакторки. ****В этом случае вас спасёт "
            "сложный пароль, который невозможно подобрать."),
        npc.Floppa.say("Пароль '''yalublukvas''' достаточно сложный?"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Не очень. Его сможет отгадать с нескольких попыток любой, кто знает тебя — например, Сорока. Попробуй лучше '''ja04[#lublu@kvas4]'''"),
        npc.Floppa.say("Не понимаю, а какая разница?"),
        npc.Owl.say(
            "Разница есть. Пароль, который ты предложил, простой, потому что он полностью состоит из "
            "слов. Лучше добавить в пароль цифры и специальные символы, чтобы его нельзя было угадать "
            "или подобрать с помощью перебора"),
        npc.Magpie.say("сложностей и так каждый день по горло, так ещё и с паролем заморачиваться"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Тогда можешь воспользоваться **генераторами паролей**. Сейчас их очень много, но лучше использовать те, "
            "которые точно не сохраняют ваши пароли на своих сервисах, например, [https://www.random.org/passwords/]("
            "https://www.random.org/passwords/) или специальную программу '''KeePass'''."),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.say("**[Сгенерировать пароль]**"),
        npc.Owl.say(
            "Есть ещё одно важное правило: нельзя ставить один и тот же пароль, каким бы сложным он ни был, "
            "на несколько сайтов. И забудьте про автозаполнение!"),
        npc.Floppa.say(
            "А как я запомню-то их все? Обвесить мой ноутбук стикерами с паролями звучит не очень безопасно..."),
        npc.Owl.say(
            "Запоминать ничего не нужно, для этого есть менеджеры паролей. Например, тот же самый '''KeePass'''. Он "
            "помнют все твои пароли и вводит их автоматически. Тебе нужно запомнить только один пароль — от самого KeePass. "),
        npc.Squirrel.say("А с корпоративными аккаунтами как быть?"),
        npc.Magpie.say("да! если с кем-то из нас что-то случится, у редакции должен остаться доступ к его данным"),
        npc.Owl.say(
            "В KeePass можно хранить не только свои пароли, но и пароли других пользователей — как раз для таких случаев. "),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "У KeePass есть куча вариантов для разных устройств и операционных систем. Найдите версию для вашего устройства "
            "и попробуйте установить: [https://keepass.info/download.html]("
            "https://keepass.info/download.html). Нажмите «Сделано», когда установите и протестируете."),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("**[Сделано!]**"),
        # ЗДЕСЬ     ———————игроки жмут на кнопку———————

        #М: ПРО КЕНГУРУ СОВСЕМ НЕ ПОНИМАЮ СЕТАП. ДЛЯ ЧЕГО ОН НУЖЕН?:) 
        npc.Owl.say(
            "Я сейчас свяжусь с моими знакомыми кенгуру из Австралии, они смогут сохранить наши пароли в безопасности"),
        npc.Owl.say("Давайте я сделаю корпоративный доступ для всех нас!"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("**[Получить корпоративный доступ]**"),
        # ЗДЕСЬ     ****———————игроки жмут на кнопку———————

        npc.Floppa.say("Ура!!! Теперь мы защищены до зубов!!"),
        npc.Magpie.say("так никто не говорит.... вооружены до зубов а не защищены"),
        npc.Squirrel.say("Сорока! А давай узнаем о случаях взлома у разных медиа и активистов?"),
        npc.Magpie.say("ок, перестаю щёлкать клювом в чате и вылетаю"),
        npc.Floppa.say("Удачи!"),
    ],
)
