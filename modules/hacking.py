from engine.glide import StoryMap
from engine.var import Var, Jump, Proceed

from modules.init import npc

description = "Взлом"

content = StoryMap(
    entry=[
        npc.Squirrel.say("Сорока, ты не знаешь, где сейчас Кролик?"),
        npc.Magpie.say("что случилось?"),
        npc.Squirrel.say("Он должен был прислать мне инфографику по беженцам "),
        npc.Magpie.say("сейчас тыкну его"),
        npc.Magpie.say("молчит"),
        npc.Magpie.say("белочка, ты связывалась с другими активистами?"),
        npc.Floppa.say("Может, он занят?"),
        npc.Magpie.say("он в сети был 10 часов назад"),
        npc.Magpie.say("а ушастый жить не может без уютных чатов с картинками"),
        npc.Floppa.say("Понимаю его... Тогда это реально странно"),
        npc.Floppa.say("Мб он уснул просто"),
        npc.Squirrel.say("У меня вроде ничего не горит, но я реально очень много волноваться начала в последнее время"),
        npc.Floppa.say("Тебе просто нужно отдохнуть!"),
        npc.Squirrel.say("Может, это было бы и неплохо"),
        npc.Squirrel.say("Но если я буду отдыхать, то буду волноваться не из-за работы, а из-за того, что я не работаю("),
        npc.Magpie.say("какой-то замкнутый круг"),
        npc.Floppa.say("Ну блин"),
        npc.Floppa.say("Попробуй подумать не о том, что ты не работаешь, а о том, как ты классно вернёшься к своим делам вся такая полная сил и духовной энергии"),
        npc.Squirrel.say("Звучит разумно вообще"),
        npc.Squirrel.say("Но мне кажется, что моя тревога снова всех переиграет)"),
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
        npc.Magpie.say("кроль, мб ты объяснишься?? ниче не хочешь мне сказать???"),
        npc.Magpie.say("там блин вообще то куча моей работы и твоей тоже"),
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
        npc.Squirrel.say("Блин, нехорошо"),
        npc.Squirrel.say("Я всех подвела"),
        npc.Floppa.say("Вы же никогда с таким не сталкивались! И ты же смогла всё исправить"),
        Proceed(password=True)
    ],
    
    password=[
        npc.Magpie.say("смотрите что выкатил наш дом"),
        npc.Magpie.say(
            "```Привет, это зайчиха Варвара. Мы потеряли связь с нашим сотрудником кроликом Степаном.  Пожалуйста, ```"
            "```сообщите нам, если вам что-либо известно.\nUPD: В телеграм-аккаунты трех наших сотрудников пытались ```"
            "```войти. ```"),
        npc.Magpie.say("жуть какая-то"),
        npc.Floppa.say("У вас раньше уже было что-то подобное? Это похоже на массовый взлом???"),
        npc.Floppa.say("Зачем они пытаются кого-то взламывать??????"),
        npc.Squirrel.say("Вот сейчас я правда начала нервничать"),
        npc.Squirrel.say("Ребят, вы хоть двухфакторкой пользуетесь?"),
        npc.Magpie.say("чем"),
        npc.Owl.say("Двухфакторной аутентификации нет ни у кого."),
        npc.Squirrel.say("Ну вы даете"),
        npc.Owl.say(
            "Двухфакторная аутентификация - это алгоритм идентификации пользователя, для выполнения которого "
            "пользователю нужно предъявить несколько (в нашем случае 2) доказательств, подтверждающих, что вы - это "
            "вы."),
        npc.Owl.say(
            "Например, если кто-то узнал ваш пароль от почты, но при этом у вас стояла двухфакторка, то этому кому-то "
            "понадобится второй фактор (обычно это смартфон, который связан с этой почтой), чтобы заполучить ваши "
            "данные."),
        npc.Owl.say(
            "К сожалению, смс-оповещения не самая безопасная вещь, поэтому вы можете установить на свои телефоны "
            "'''OTP '''Auth''' для iOS и '''andOTP''' для android - они сами связываются с сервисами и "
            "генерируют коды подтверждения."),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("**[Установить двухфакторную аутентификацию]**"),
        npc.Floppa.say(
            "Ха, то есть мой телефон - это золотой ключик?) А если его заберёт себе какая-нибудь черепаха? Как я "
            "тогда попаду в свой театр???"),
        npc.Owl.say(
            "Для этого вам нужно позаботиться ещё об одном моменте - **резервных кодах**. Резервные коды это целый "
            "список ваших личных кодов, созданный вашим сервисом или программой для генерации кодов, как раз на тот "
            "случай, если у вас нет доступа телефону."),
        npc.Owl.say(
            "У всех вас наверняка есть аккаунты в гугле! Если у вас нет двухфакторки там, то обязательно установите. "
            "А потом скачайте свои резервные коды оттуда, но помните, что каждый из них работает только один раз."),
        npc.Squirrel.say("Напишите мне готово, когда закончите!"),
        npc.Floppa.say("Слушайте"),
        npc.Floppa.say("А если в сервисе, которым я пользуюсь, нет двухфакторки? Что тогда делать?"),
        npc.Magpie.say("тогда, наверное, не стоит им пользоваться"),
        npc.Floppa.say("Но ведь там скидки на квас..."),
        npc.Magpie.say("кому нужны твои скидки"),
        npc.Owl.say("Спокойно! Никто не потеряет никаких скидок."),
        npc.Owl.say(
            "Но Флоппа правильно сказал, что есть сервисы без двухфакторки. ****Теперь вам нужно заменить все ваши "
            "пароли на более сложные."),
        npc.Floppa.say("Пароль '''yalublukvas''' достаточно сложный?"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Не очень. Зная тебя, даже Сорока сможет его подобрать. Попробуй лучше '''ja04[#lublu@kvas4]'''"),
        npc.Floppa.say("Не понимаю, а какая разница?"),
        npc.Owl.say(
            "Разница есть. Пароль, который ты предложил, простой, потому что он полностью состоит из "
            "слов. Кроме того, в нём не хватает цифр и специальных символов."),
        npc.Owl.say(
            "В действительно сложных паролях обязательно присутствуют спецсимволы, цифры и в них, как правило, "
            "нет слов."),
        npc.Magpie.say("сложного и так каждый день по горло, так ещё и с паролем заморачиваться"),
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
            "Запоминать ничего не нужно, для этого есть менеджеры паролей. Например, тот же самый '''KeePass'''. Эта "
            "программа мультиплатформенная, вы можете поставить их на любые устройства с любой оперативной системой. "),
        npc.Squirrel.say("Ну это всё личные, а с корпоративными аккаунтами что?"),
        npc.Magpie.say("да! если с кем-то из нас что-то случится у редакции должен остаться доступ к его данным"),
        npc.Owl.say(
            "Есть и такие менеджеры! Большинство из них позволяет надёжно хранить пароли сразу нескольким "
            "пользователям как раз для таких случаев. Вот в как раз в KeePass можно не только держать свои пароли, "
            "но и добавлять пароли других пользователей. Главное, что эта программа имеет открытый код и полностью "
            "бесплатна для вас!"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info(
            "Посмотрите, как много у нее вариантов! [https://keepass.info/download.html]("
            "https://keepass.info/download.html) - тут и для айфона, и для айпада есть! Кликните на эту ссылку, "
            "найдите версию для своего устройства и протестируйте! Нажмите на кнопку ниже, когда закончите."),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("**[Сделано!]**"),
        # ЗДЕСЬ     ———————игроки жмут на кнопку———————

        npc.Owl.say(
            "Я сейчас свяжусь с моими знакомыми кенгуру из Австралии, они смогут сохранить наши пароли в безопасности"),
        npc.Owl.say("Давайте я сделаю корпоративный доступ для всех нас!"),
        # В СТРОКЕ НИЖЕ ДОЛЖНА БЫТЬ КНОПКА
        npc.Owl.info("**[Получить корпоративный доступ]**"),
        # ЗДЕСЬ     ****———————игроки жмут на кнопку———————

        npc.Floppa.say("Ура!!! Теперь мы защищены до зубов!!"),
        npc.Magpie.say("так никто не говорит.... вооружены до зубов а не защищены"),
        npc.Squirrel.say("Сорока! А давай узнаем о случаях взлома у разных медиа и активистов"),
        npc.Magpie.say("всё перестаю щёлкать клювом в чате и вылетаю"),
        npc.Floppa.say("Удачи"),
    ],
)
