from engine.glide import StoryMap
from engine.var import Var, Jump, Proceed

from modules.init import npc, score

description = "Взлом"

content = StoryMap(
    entry=[
        npc.Squirrel.say("Сорока, ты не знаешь, где сейчас Кролик?"),
        npc.Magpie.say("что случилось?"),
        npc.Squirrel.say("Он должен был прислать мне инфографику по беженцам "),
        npc.Magpie.say("сейчас наберу его"),
        npc.Floppa.say("....."),
        npc.Floppa.say("............ ждем"),
        npc.Floppa.say("...."),
        npc.Magpie.say("не отвечает"),
        npc.Floppa.say("Может, занят?"),
        npc.Magpie.say("он в сети был 10 часов назад"),
        npc.Magpie.say("а ушастый жить не может без уютных чатов с картинками"),
        npc.Floppa.say("Понимаю его... Тогда это реально странно"),
        npc.Floppa.say("Мб он уснул просто"),
        npc.Rabbit.say("Здравствуйте, коллеги!"),
        npc.Rabbit.info(
            "С прискорбием сообщаю от лица нашей организации о закрытии лагеря. Эти животные совершенно не хотят жить "
            "по правилам, поэтому мы вынуждены прекратить нашу деятельность."),
        npc.Floppa.say("Чегоо???"),
        npc.Squirrel.say("Эээ."),
        npc.Rabbit.say(
            "Мы просим удалить вас все материалы о нашей организации и лагере. Мы действительно хотели бы забыть эту историю."),
        npc.Floppa.say("А что с беженцами?"),
        npc.Rabbit.say("Мы перенаправим их в другие убежища. "),
        npc.Squirrel.say(
            "По нашей редакционной политике мы не удаляем опубликованные материалы. Но можем опубликовать ваш комментарий по поводу закрытия шелтера"),
        npc.Floppa.say("Что у вас случилось??????"),
        npc.Rabbit.info(
            "Мы дадим комментарий только в обмен на удаление материалов. К сожалению, никак иначе мы не можем, "
            "это нужно в целях безопасности."),
        npc.Floppa.say("Кролик?"),
        npc.Floppa.say("Мне это не нравится"),
        npc.Floppa.say("Белка, это очень странно. Кролика могли взломать?"),
        npc.Squirrel.say("Не знаю"),
        npc.Magpie.say("кроль, мб ты объяснишься? ниче не хочешь мне сказать???"),
        npc.Magpie.say("там вообще то куча моей работы, и твоей тоже"),
        npc.Magpie.say("ушастый не берёт трубку"),
        npc.Magpie.say("класс"),
        npc.Squirrel.say("Так его реально взломали?"),
        npc.Squirrel.say("Мне бы не хотелось, чтобы наша переписка оказалась в чьих-то лапах..."),
        npc.Squirrel.say("Давайте проголосуем! Если вы считаете, что Кролика взломали, я удалю его из чата"),
        # В СТРОКЕ НИЖЕ ДОЛЖНО БЫТЬ ГОЛОСОВАНИЕ
        npc.Squirrel.ask("Кролик взломан?", [("Взломан", "hacked"), ("Не взломан", "not_hacked")], Var.rabbit_hacked),
        Jump(Var.rabbit_hacked)
        # ЗДЕСЬ     ****———————игроки голосуют———————
    ],

    hacked=[
        #    - **ПОСЛЕДСТВИЯ: Кролик взломан!**

        npc.Squirrel.kick(npc.Rabbit),
        npc.Squirrel.say("Надеюсь, мы поступили правильно."),
        Proceed(password=True)
    ],

    not_hacked=[
        #    - **ПОСЛЕДСТВИЯ: Кролик не взломан!**

        npc.Squirrel.say("Ладно, Кролик."),
        npc.Squirrel.say("Сейчас я уберу заметки с сайта."),
        score.add(-2),
        npc.Squirrel.say("..."),
        npc.Squirrel.say("Мне только что позвонили из Нашего Дома"),
        npc.Squirrel.say("Кролика всё-таки взломали..."),
        npc.Squirrel.kick(npc.Rabbit),
        npc.Floppa.say("Ты же можешь вернуть материалы?"),
        npc.Squirrel.say("Конечно, сейчас"),
        npc.Squirrel.say("Блин, ситуация отстой"),
        npc.Floppa.say("Ничего страшного, мы просто никогда с таким не сталкивались!"),
        npc.Floppa.say("И ты ведь смогла всё исправить"), 
        Proceed(password=True)
    ],
    
    password=[
        npc.Magpie.say("смотрите, что выкатил наш дом"),
        npc.Magpie.say(
            "``` Привет, это зайчиха Варвара. Мы потеряли связь с нашим сотрудником кроликом Степаном. Пожалуйста,"
            "сообщите нам, если вам что-либо известно.\n"
            "UPD: В телеграм-аккаунты трех наших сотрудников пытались войти. ```"),
        npc.Magpie.say("жуть какая-то"),
        npc.Floppa.say("У вас раньше уже было что-то подобное? Это похоже на массовый взлом???"),
        npc.Floppa.say("Зачем они пытаются кого-то взламывать??????"),
        npc.Squirrel.say("Я одна не понимаю, на что они надеются?"),
        npc.Squirrel.say("Ведь чтобы зайти в Телеграм с нового устройства, нужен смс-код"),
        npc.Squirrel.say("Они же не могут его получить... Или как?"),
        npc.Owl.say("Ну вообще могут."),
        npc.Owl.say("SMS-сообщения можно перехватить."),
        npc.Owl.say("Именно поэтому рекомендую всем настроить двухфакторную аутентификацию."),
        npc.Owl.info(
            "Если у вас стоит двухфакторная аутентификация, то для запуска вашего Telegram на "
            "другом устройстве понадобится не только SMS-код, но и специальный пароль, который "
            "знаете только вы. "),
        npc.Owl.info(
            "Чтобы установить двухфакторку в Telegram, перейдите в Настройки — Конфиденциальность — Облачный пароль. "
            "После ввода пароля вас попросят придумать подсказку к нему и указать электронную почту, куда "
            "придёт проверочный код для подтверждения пароля. Введите его в соответствующее поле — вуаля, "
            "двухфакторка установлена."),
        npc.Squirrel.say("Я себе поставила на прошлых выходных! Чувствую себя спокойнее"),
        npc.Squirrel.say("А двухфакторка есть только в Телеграме?"),
        npc.Owl.say("Её можно подключить для большинства сервисов и соцсетей — в том числе Instagram, Facebook, Gmail. "),
        npc.Owl.say("Только в этом случае всё будет наоборот. Так как обычно вы входите в соцсети с помощью пароля, сервис "
                    "попросит вас привязать аккаунт к телефону. "),
        npc.Floppa.say("Но ты же только что сказала, что смски небезопасны...."),
        npc.Owl.say("Флоппа, позволь мне закончить. :)"),
        npc.Owl.info("Так как SMS-сообщения можно перехватить, рекомендую вам установить на телефоны приложения "
                    "`OTPAuth` для iPhone и `andOTP` для Android. Если у вас уже стоит аналичные аутентификаторы"
                    "Когда вы привяжете свои аккаунты к этим "
                    "приложениям, секретные коды будут приходить не в виде SMS, вы просто получите их в приложении"),
        #npc.Floppa.say(
        #    "Ха, то есть мой телефон - это золотой ключик?) А если его заберёт какая-нибудь черепаха? Как я "
        #    "тогда попаду в свой театр???"),
#        npc.Owl.say(
#            "Для этого тебе нужно выпустить **резервные коды**. Любой из резервных кодов "
#            "можно ввести вместо секретного кода. Так ты сможешь войти в любой аккаунт, даже если потеряешь телефон."),

         #М: В СООБЩЕНИЕ СОВЫ ВСТАВИТЬ БЫ КАКОЙ-ТО СКРИН, КОТОРЫЙ ПОКАЖЕТ, КАК ВЫГЛЯДЯТ РЕЗЕРВНЫЕ КОДЫ, НАПРИМЕР: https://help.mail.ru/pic/4/6/4699cf9690329de953b0df51ff64c63a.png
#        npc.Owl.say(
#            "Их несколько, и каждый из них работает только один раз. Поэтому лучше всего распечатать этот"
#            "список или где-то записать. "),
#        npc.Magpie.say("а их безопасно вот так просто хранить? "),
#        npc.Magpie.say("вдруг кто-то увидит их у меня в гнезде и заберёт??"),
#        npc.Owl.say(
#            "Никто, кроме тебя, не знает, что это за наборы цифр и что с ними делать. "
#            "Запомнить все коды невозможно, поэтому лучше так. "),
#        npc.Owl.say("Давайте потренируемся на примере аккаунтов в Google — они наверняка есть у всех. Установите "
#                    "себе двухфакторную аутентификацию, а потом скачайте и распечатайте свои резервные коды. "),
#        npc.Owl.info("Переходите по ссылке и следуйте инструкциям, это займёт 5 минут: [https://bit.ly/3tH5xiq]("
#            "https://bit.ly/3tH5xiq)", button_text="Сделали"),
#        npc.Squirrel.say("Прекрасно!"),
        npc.Floppa.say("Слушайте"),
        npc.Floppa.say("А если в сервисе, которым я пользуюсь, нет двухфакторки? Что тогда делать?"),
        npc.Magpie.say("тогда, наверное, не стоит им пользоваться"),
        npc.Floppa.say("Но ведь там скидки на квас..."),
        npc.Magpie.say("кому нужны твои скидки"),
        npc.Owl.say("Спокойно! Никто не потеряет никаких скидок."),
        npc.Owl.say(
            "Но Флоппа правильно сказал, что есть сервисы без двухфакторки. В этом случае особенно важен надежный пароль."),
        npc.Floppa.say("Пароль `yalublukvas` достаточно надежен?"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Не очень. Его сможет отгадать с нескольких попыток любой, кто знает тебя — например, Сорока. Попробуй лучше `ja04#lublu@kvas4`"),
        npc.Floppa.say("Не понимаю, а какая разница?"),
        npc.Owl.say(
            "Разница есть. Пароль, который ты предложил, простой, потому что он полностью состоит из "
            "слов. Лучше добавить в пароль цифры и специальные символы, чтобы его нельзя было угадать "
            "или подобрать."),
        npc.Owl.info(
            "Есть ещё одно важное правило: нельзя ставить один и тот же пароль, каким бы сложным он ни был, "
            "на несколько сайтов."),
        npc.Floppa.say(
            "А как я запомню-то их все? Обвесить мой ноутбук стикерами с паролями звучит не очень безопасно..."),
        npc.Owl.info(
            "Запоминать ничего не нужно, для этого есть менеджеры паролей. Лично я рекомендую `BitWarden` и `KeePassXC`. "
            "Тебе нужно запомнить только один пароль — от самого менджера. И раз ты будешь хранить пароли там, то лучше отключить автозаполнение паролей в браузере."), # tdodo генерация паролей
        npc.Squirrel.say("А с корпоративными аккаунтами как быть?"),
        npc.Magpie.say("да! если с кем-то из нас что-то случится, у редакции должен остаться доступ к его данным"),
        npc.Owl.info("Именно поэтому я советую в первую очередь `BitWarden` -- он подразумевает облачную синхронизацию"),
        # пиу пиу
        
        #М: ПРО КЕНГУРУ СОВСЕМ НЕ ПОНИМАЮ СЕТАП. ДЛЯ ЧЕГО ОН НУЖЕН?:) 
        #npc.Owl.info(
        #    "Я сейчас свяжусь с моими знакомыми кенгуру из Австралии, они смогут сохранить наши пароли в безопасности"),
        #npc.Owl.say("Давайте я сделаю корпоративный доступ для всех нас!", button_text=),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        #npc.Owl.info("**[Получить корпоративный доступ]**"),
        # ЗДЕСЬ     ****———————игроки жмут на кнопку———————

        npc.Floppa.say("Ура!!! Теперь мы защищены до зубов!!"),
        npc.Magpie.say("так никто не говорит.... вооружены до зубов а не защищены"),
        npc.Squirrel.say("Сорока! А давай узнаем о случаях взлома у разных медиа и активистов?"),
        npc.Magpie.say("ок, перестаю щёлкать клювом в чате и вылетаю"),
        npc.Floppa.say("Удачи!"),

        Proceed(game_break=True)
    ],

    game_break=[
        npc.Squirrel.ask(
            "Ребята, вы очень хорошо потрудились. Предложу вам чуть-чуть отдохнуть, заварить себе чай."
            "Возвращайтесь, когда почувствуете, что у вас есть силы продолжить игру.",
            [("Отдохнули", "relax")], Var.null),
        # Proceed(vzlom=True)
        # КОРЖ: ТУТ ВООБЩЕ ДОЛЖНО БЫТЬ МЕНЮ С ВЫБОРОМ СЛЕДУЮЩЕГО БЛОКА
        # М: ТУТ БЫ ЕЩЁ СОСЛАТЬСЯ НА ВРЕМЕННЫЕ ОТСЕЧКИ: МОЛ, ВЫ ПРОШЛИ ТРЕТЬ ИЛИ ПОЛОВИНУ ИГРЫ, ВПЕРЕДИ ЕЩЁ ПОЛЧАСА ПРИМЕРНО. ПРЕДЛОЖУ, КОГДА СМОГУ ВСЁ ПОТЕСТИРОВАТЬ И ЗАСЕЧЬ
    ]
)
