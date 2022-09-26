import telebot
from telebot import types

bot = telebot.TeleBot('5634375605:AAETwJSyOylRX80MZKK8Tq_SxC48epUPlBs')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Информация о ВУЗе")
    btn2 = types.KeyboardButton("Задать вопрос")
    btn3 = types.KeyboardButton("Электронные ресурсы")
    btn4 = types.KeyboardButton("Общежития")
    btn5 = types.KeyboardButton("Информация об онлайн-оплате")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот-помощник для студента УМЦ".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Информация о ВУЗе":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Бакалавриат")
        btn2 = types.KeyboardButton("Магистратура")
        btn3 = types.KeyboardButton("Аспирантура")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите категорию".format(message.from_user), reply_markup=markup)
    elif message.text == "Бакалавриат":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Направления подготовки бакалавриата")
        btn2 = types.KeyboardButton("Стоимость обучения на бакалавриате")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задайте вопрос".format(message.from_user), reply_markup=markup)
    elif message.text == "Стоимость обучения на бакалавриате":
        img1 = open("photos/Очная_бакалавриат.JPG", "rb")
        bot.send_message(message.chat.id, text="Очная форма обучения")
        bot.send_photo(message.chat.id, img1)
        img2 = open("photos/Очно-заочная_бакалавриат.jpg", "rb")
        bot.send_message(message.chat.id, text="Очно-заочная форма обучения")
        bot.send_photo(message.chat.id, img2)
        img3 = open("photos/Заочная_бакалавриат.jpg", "rb")
        bot.send_message(message.chat.id, text="Заочная форма обучения")
        bot.send_photo(message.chat.id, img3)
    elif message.text == "Направления подготовки бакалавриата":
        markup = types.InlineKeyboardMarkup()
        bak1 = types.InlineKeyboardButton(text='Политология', url='http://imc-i.ru/polit/')
        bak2 = types.InlineKeyboardButton(text='Психология', url='http://imc-i.ru/psixologiya/')
        bak3 = types.InlineKeyboardButton(text='Юриспруденция', url='http://imc-i.ru/yuridicheskij/')
        bak4 = types.InlineKeyboardButton(text='Реклама и связи с общественностью', url='http://imc-i.ru/rekl/')
        bak5 = types.InlineKeyboardButton(text='Зарубежное регионоведение', url='http://imc-i.ru/region/')
        bak6 = types.InlineKeyboardButton(text='Международные отношения', url='http://imc-i.ru/mo/')
        bak7 = types.InlineKeyboardButton(text='Экономика', url='http://imc-i.ru/econom/')
        bak8 = types.InlineKeyboardButton(text='Менеджмент', url='http://imc-i.ru/manag/')
        bak9 = types.InlineKeyboardButton(text='Государственное и муниципальное управление', url='http://imc-i.ru/gmu/')
        bak10 = types.InlineKeyboardButton(text='Бизнес-информатика', url='http://imc-i.ru/bussines/')
        bak11 = types.InlineKeyboardButton(text='Дизайн', url='http://imc-i.ru/dizain/')
        bak12 = types.InlineKeyboardButton(text='Лингвистика', url='http://imc-i.ru/lingvistika/')
        bak13 = types.InlineKeyboardButton(text='Журналистика', url='http://imc-i.ru/zhurnalistika/')

        markup.add(bak1, bak2, bak3, bak4, bak5, bak6, bak7, bak8, bak9, bak10, bak11, bak12, bak13)
        bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
    elif message.text == "Магистратура":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Направления подготовки магистратуры")
        btn2 = types.KeyboardButton("Стоимость обучения на магистратуре")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задайте вопрос".format(message.from_user), reply_markup=markup)
    elif message.text == "Направления подготовки магистратуры":
        markup = types.InlineKeyboardMarkup()
        mag1 = types.InlineKeyboardButton(text='Политология',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/politologia/')
        mag2 = types.InlineKeyboardButton(text='Психология',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/psixologiya/')
        mag3 = types.InlineKeyboardButton(text='Юриспруденция',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/yuridicheskij/')
        mag4 = types.InlineKeyboardButton(text='Зарубежное регионоведение',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/zarubezhnoe-regionovedenie/')
        mag5 = types.InlineKeyboardButton(text='Международные отношения',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/mo/')
        mag6 = types.InlineKeyboardButton(text='Экономика',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/economika/')
        mag7 = types.InlineKeyboardButton(text='Государственное и муниципальное управление',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/gmu')
        mag8 = types.InlineKeyboardButton(text='Дизайн',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/dizain/')
        mag9 = types.InlineKeyboardButton(text='Лингвистика',
                                          url='http://imc-i.ru/magistratura/magisterskie-programmy/lingvistika/')
        mag10 = types.InlineKeyboardButton(text='Журналистика',
                                           url='http://imc-i.ru/magistratura/magisterskie-programmy/zhurnalistika/')

        markup.add(mag1, mag2, mag3, mag4, mag5, mag6, mag7, mag8, mag9, mag10)
        bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
    elif message.text == "Стоимость обучения на магистратуре":
        img1 = open("photos/Очная_магистратура.jpg", "rb")
        bot.send_message(message.chat.id, text="Очная форма обучения")
        bot.send_photo(message.chat.id, img1)
        img2 = open("photos/Очно-заочная_магистратура.jpg", "rb")
        bot.send_message(message.chat.id, text="Очно-заочная форма обучения")
        bot.send_photo(message.chat.id, img2)
        img3 = open("photos/Заочная_магистратура.jpg", "rb")
        bot.send_message(message.chat.id, text="Заочная форма обучения")
        bot.send_photo(message.chat.id, img3)
    elif message.text == "Аспирантура":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Направления подготовки аспирантуры")
        btn2 = types.KeyboardButton("Стоимость обучения на аспирантуре")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задайте вопрос".format(message.from_user), reply_markup=markup)
    elif message.text == "Стоимость обучения на аспирантуре":
        img1 = open("photos/Очная_аспирантура.jpg", "rb")
        bot.send_message(message.chat.id, text="Очная форма обучения")
        bot.send_photo(message.chat.id, img1)
        img2 = open("photos/Заочная_аспирантура.jpg", "rb")
        bot.send_message(message.chat.id, text="Заочная форма обучения")
        bot.send_photo(message.chat.id, img2)
    elif message.text == "Направления подготовки аспирантуры":
        markup = types.InlineKeyboardMarkup()
        asp1 = types.InlineKeyboardButton(text='Психология труда, инженерная психология, когнитивная эргономика',
                                          url='http://imc-i.ru/psiholog/')
        asp2 = types.InlineKeyboardButton(text='Региональная и отраслевая экономика', url='http://imc-i.ru/economika/')
        asp3 = types.InlineKeyboardButton(text='Политические институты, процессы, технологии',
                                          url='http://imc-i.ru/politicheskie-nauki-i-regionovedenie/')

        markup.add(asp1, asp2, asp3)
        bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
    elif message.text == "Задать вопрос":
        markup = types.InlineKeyboardMarkup()
        que1 = types.InlineKeyboardButton(text='Контакты', url='http://imc-i.ru/abiturientam/kontakty/')

        markup.add(que1)
        bot.send_message(message.chat.id, "Вы можете задать вопрос напрямую в ВУЗ", reply_markup=markup)
    elif message.text == "Электронные ресурсы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Органы государственной власти")
        btn2 = types.KeyboardButton("Федеральные образовательные порталы")
        btn3 = types.KeyboardButton("Сетевые СМИ")
        btn4 = types.KeyboardButton("Информационно-аналитические обзоры СМИ")
        btn5 = types.KeyboardButton("Общественно-политические периодические издания")
        btn6 = types.KeyboardButton("Научные журналы")
        btn7 = types.KeyboardButton("Правовые информационные системы")
        btn8 = types.KeyboardButton("Электронно-библиотечные системы")
        btn9 = types.KeyboardButton("Тематические сайты и электронные библиотеки")
        btn10 = types.KeyboardButton("Энциклопедии, словари, справочные ресурсы")
        btn11 = types.KeyboardButton("Сайты антиэкстремистского и антитеррористического содержания")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, back)
        bot.send_message(message.chat.id, text="Выберите тип электронного ресурса".format(message.from_user),
                         reply_markup=markup)
    elif message.text == "Органы государственной власти":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Сервер органов государственной власти Официальная Россия',
                                          url='http://www.gov.ru/')
        btn2 = types.InlineKeyboardButton(text='Правительство Российской Федерации: Интернет-портал',
                                          url='http://government.ru/')
        btn3 = types.InlineKeyboardButton(text='Официальный сайт Мэра и Правительства Москвы', url='http://www.mos.ru/')

        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Федеральные образовательные порталы":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Официальный сайт Министерства образования и науки Российской Федерации',
                                          url='https://минобрнауки.рф/')
        btn2 = types.InlineKeyboardButton(
            text='Официальный сайт Федеральной службы по надзору в сфере образования и науки',
            url='http://obrnadzor.gov.ru/')
        btn3 = types.InlineKeyboardButton(text='Федеральный портал «Российское образование»', url='http://www.edu.ru/')
        btn4 = types.InlineKeyboardButton(
            text='Информационная система «Единое окно доступа к образовательным ресурсам»', url='http://window.edu.ru/')
        btn5 = types.InlineKeyboardButton(text='Федеральный центр информационно-образовательных ресурсов',
                                          url='http://fcior.edu.ru/')
        btn6 = types.InlineKeyboardButton(text='Федеральный образовательный портал Экономика-Социология-Менеджмент',
                                          url='http://www.ecsocman.hse.ru/')
        btn7 = types.InlineKeyboardButton(text='Юридическая Россия — Федеральный правовой портал',
                                          url='http://law.edu.ru/')
        btn8 = types.InlineKeyboardButton(text='Университетская информационная система РОССИЯ',
                                          url='http://uisrussia.msu.ru/')
        btn9 = types.InlineKeyboardButton(text='Единая коллекция цифровых образовательных ресурсов',
                                          url='http://school-collection.edu.ru/')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Сетевые СМИ":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='«Газета.ру»',
                                          url='http://www.gazeta.ru/')
        btn2 = types.InlineKeyboardButton(
            text='«Вести.ру»',
            url='http://www.vesti.ru/')
        btn3 = types.InlineKeyboardButton(text='«Утро.ру»', url='http://www.utro.ru/')
        btn4 = types.InlineKeyboardButton(
            text='«Лента.ру»', url='http://www.lenta.ru/')
        btn5 = types.InlineKeyboardButton(text='Агентство национальных новостей',
                                          url='http://www.annews.ru/')
        btn6 = types.InlineKeyboardButton(text='Агентство экономической информации «Прайм»',
                                          url='http://www.1prime.ru/')
        btn7 = types.InlineKeyboardButton(text='Политические новости России «Полит.ру»',
                                          url='http://www.polit.ru/')
        btn8 = types.InlineKeyboardButton(text='Агентство политических новостей «АПН.ру»',
                                          url='http://www.apn.ru/')
        btn9 = types.InlineKeyboardButton(text='Научно-технический центр правовой информации',
                                          url='http://www.systema.ru/')
        btn10 = types.InlineKeyboardButton(text='Портал электронных СМИ для предпринимателей',
                                           url='http://www.businesspress.ru/')
        btn11 = types.InlineKeyboardButton(text='Российское агентство научных новостей «Информнаука»',
                                           url='http://www.informnauka.ru/')
        btn12 = types.InlineKeyboardButton(text='Агентство культурной информации',
                                           url='http://www.aki-ros.ru/')
        btn13 = types.InlineKeyboardButton(text='Агентство культурных и бизнес-коммуникаций',
                                           url='http://www.cultcom.ru/')
        btn14 = types.InlineKeyboardButton(text='Российская культура в событиях и лицах',
                                           url='http://www.rosculture.ru/')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Информационно-аналитические обзоры СМИ":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Polpred.com',
                                          url='http://polpred.com/')
        btn2 = types.InlineKeyboardButton(text='Каталог World-newspapers',
                                          url='http://www.world-newspapers.com/')
        btn3 = types.InlineKeyboardButton(text='Ingenta', url='http://www.ingentaconnect.com/')

        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Общественно-политические периодические издания":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='«Российская газета»',
                                          url='http://www.rg.ru/')
        btn2 = types.InlineKeyboardButton(text='«Коммерсантъ»',
                                          url='http://www.kommersant.ru/')
        btn3 = types.InlineKeyboardButton(text='«Независимая газета»', url='http://www.ng.ru/')
        btn4 = types.InlineKeyboardButton(text='«Новая газета»',
                                          url='http://www.novayagazeta.ru/')
        btn5 = types.InlineKeyboardButton(text='«Профиль»',
                                          url='http://www.profile.ru/')
        btn6 = types.InlineKeyboardButton(text='«Эксперт»', url='http://www.expert.ru/')
        btn7 = types.InlineKeyboardButton(text='«Аргументы и факты»',
                                          url='http://www.aif.ru/')
        btn8 = types.InlineKeyboardButton(text='«Московский комсомолец»',
                                          url='http://www.mk.ru/')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Научные журналы":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='eLIBRARY.RU — научная электронная библиотека',
                                          url='http://elibrary.ru/')
        btn2 = types.InlineKeyboardButton(text='BioOne',
                                          url='http://www.bioone.org/')
        btn3 = types.InlineKeyboardButton(text='Журнал «Pro et Contra»', url='http://carnegie.ru/proetcontra')
        btn4 = types.InlineKeyboardButton(text='Демоскоп Weekly',
                                          url='http://demoscope.ru/')
        btn5 = types.InlineKeyboardButton(text='Ежегодники SIPRI',
                                          url='http://www.sipri.org/yearbook')
        btn6 = types.InlineKeyboardButton(text='МЕДИАСКОП', url='http://mediascope.ru/')
        btn7 = types.InlineKeyboardButton(text='Политическая концептология: журнал метадисциплинарных исследований',
                                          url='http://politconcept.sfedu.ru/')
        btn8 = types.InlineKeyboardButton(text='Региональная экономика и управление: электронный научный журнал',
                                          url='http://region.mcnip.ru/')
        btn9 = types.InlineKeyboardButton(text='Россия и Америка в XXI веке', url='http://www.rusus.ru/')
        btn10 = types.InlineKeyboardButton(text='Социальные аспекты здоровья населения',
                                           url='http://vestnik.mednet.ru/')
        btn11 = types.InlineKeyboardButton(text='Журнал «Теоретическая экономика»',
                                           url='http://www.ystu.ru/science/Theoretical_economics/')
        btn12 = types.InlineKeyboardButton(text='Журнал «Управление экономическими системами»', url='http://uecs.ru/')
        btn13 = types.InlineKeyboardButton(text='Экономическая социология',
                                           url='http://ecsoc.hse.ru/')
        btn14 = types.InlineKeyboardButton(text='Электронное приложение к «Российскому юридическому журналу»',
                                           url='http://electronic.ruzh.org/')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Правовые информационные системы":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='«КонсультантПлюс»',
                                          url='https://www.consultant.ru')
        btn2 = types.InlineKeyboardButton(text='Информационно-правовой портал ГАРАНТ',
                                          url='http://www.garant.ru/')
        btn3 = types.InlineKeyboardButton(text='«Референт»', url='http://www.referent.ru/')

        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Электронно-библиотечные системы":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Электронно-библиотечная система IPRbooks',
                                          url='http://www.iprbookshop.ru/')
        btn2 = types.InlineKeyboardButton(text='Электронно-библиотечная система Юрайт',
                                          url='http://www.biblio-online.ru/')

        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Тематические сайты и электронные библиотеки":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='arXiv.org',
                                          url='http://arxiv.org/')
        btn2 = types.InlineKeyboardButton(text='Astrolab',
                                          url='http://www.astrolab.ru/')
        btn3 = types.InlineKeyboardButton(text='Audit-it.ru',
                                          url='http://www.audit-it.ru/')
        btn4 = types.InlineKeyboardButton(text='Classics in the History of Psychology',
                                          url='http://psychclassics.yorku.ca/')
        btn5 = types.InlineKeyboardButton(text='DOAJ (Directory of Open Access Journals)',
                                          url='http://www.doaj.org/')
        btn6 = types.InlineKeyboardButton(text='E-Lingvo.net',
                                          url='http://www.e-lingvo.net/')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Энциклопедии, словари, справочные ресурсы":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Большая советская энциклопедия',
                                          url='http://bse.sci-lib.com/')
        btn2 = types.InlineKeyboardButton(text='Encyclopedia.com',
                                          url='http://encyclopedia.com/')
        btn3 = types.InlineKeyboardButton(text='Британника',
                                          url='http://britannica.com/')
        btn4 = types.InlineKeyboardButton(text='QUID',
                                          url='http://quid.com/')
        btn5 = types.InlineKeyboardButton(text='Bartleby.com',
                                          url='http://bartleby.com/')
        btn6 = types.InlineKeyboardButton(text='Мегаэнциклопедия Кирилла и Мефодия',
                                          url='http://www.megabook.ru/')
        btn7 = types.InlineKeyboardButton(text='Энциклопедия «Кругосвет»',
                                          url='http://www.krugosvet.ru/')
        btn8 = types.InlineKeyboardButton(text='Русский биографический словарь',
                                          url='http://rulex.ru/')
        btn9 = types.InlineKeyboardButton(text='Мир энциклопедий',
                                          url='http://encyclopedia.ru/')

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Сайты антиэкстремистского и антитеррористического содержания":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Наука и образование против террора',
                                          url='http://scienceport.ru/')
        btn2 = types.InlineKeyboardButton(
            text='Национальный центр информационного противодействия терроризму и экстремизму',
            url='http://нцпти.рф/')

        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Выберите нужное", reply_markup=markup)
    elif message.text == "Общежития":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Вся информация об общежитиях', url='http://imc-i.ru/userfiles/ufiles'
                                                                                   '/obschezhitie_prez.pdf')

        markup.add(btn1)
        bot.send_message(message.chat.id, "Памятка по общежитиям", reply_markup=markup)
    elif message.text == "Информация об онлайн-оплате":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как оплатить банковской картой")
        btn2 = types.KeyboardButton("Описание процесса передачи данных")
        btn3 = types.KeyboardButton("Возврат денежных средств")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите нужное".format(message.from_user), reply_markup=markup)
    elif message.text == "Как оплатить банковской картой":
        bot.send_message(message.chat.id,
                         text="1) Перейдите по ссылке: «http://imc-i.ru/oplata/»".format(message.from_user))
        bot.send_message(message.chat.id,
                         text="2) Заполните требуемые поля. Поля, отмеченные «*», обязательны для заполнения. "
                              "Обратите внимание! Если сумма оплаты содержит «копейки», то после цифры «рублей», "
                              "необходимо ставить (.), а не (,). Например, 12000.68".format(
                             message.from_user))
        bot.send_message(message.chat.id, text="3) Нажмите кнопку «Оплатить».".format(message.from_user))
        bot.send_message(message.chat.id,
                         text="4) Далее вы будете перенаправлены на платежный шлюз, где сможете указать реквизиты "
                              "Вашей банковской карты. Соединение с платежным шлюзом и передача параметров Вашей "
                              "пластиковой карты осуществляется в защищенном режиме с использованием 128-битного "
                              "протокола шифрования SSL. Если Банк-Эмитент вашей пластиковой карты поддерживает "
                              "технологию безопасного проведения интернет-платежей Verified By VISA или MasterCard "
                              "SecureCode, будьте готовы указать специальный пароль, необходимый для успешной оплаты. "
                              "Способы и возможность получения пароля для совершения интернет-платежа Вы можете "
                              "уточнить в банке, выпустившем Вашу карту.".format(message.from_user))
    elif message.text == "Описание процесса передачи данных":
        bot.send_message(message.chat.id,
                         text="Для оплаты Вы будете перенаправлены на платежный шлюз ОАО «Сбербанк России» для ввода "
                              "реквизитов Вашей карты. Пожалуйста, приготовьте Вашу пластиковую карту заранее. "
                              "Соединение с платежным шлюзом и передача информации осуществляется в защищенном режиме "
                              "с использованием протокола шифрования SSL. В случае если Ваш банк поддерживает "
                              "технологию безопасного проведения интернет-платежей Verified By Visa или MasterCard "
                              "Secure Code для проведения платежа также может потребоваться ввод специального пароля. "
                              "Способы и возможность получения паролей для совершения интернет-платежей Вы можете "
                              "уточнить в банке, выпустившем карту. Настоящий сайт поддерживает 128-битное "
                              "шифрование. Конфиденциальность сообщаемой персональной информации обеспечивается ОАО "
                              "«Сбербанк России». Введенная информация не будет предоставлена третьим лицам за "
                              "исключением случаев, предусмотренных законодательством РФ. Проведение платежей по "
                              "банковским картам осуществляется в строгом соответствии с требованиями платежных "
                              "систем Visa Int. и MasterCard Europe Sprl.".format(message.from_user))
    elif message.text == "Возврат денежных средств":
        bot.send_message(message.chat.id,
                         text="Возврат денежных средств при оплате банковской картой осуществляется на ту банковскую "
                              "карту, с которой был сделан платеж. Срок возврата от 1 до 30 рабочих дней.".format(message.from_user))
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        button1 = types.KeyboardButton("Информация о ВУЗе")
        button2 = types.KeyboardButton("Задать вопрос")
        button3 = types.KeyboardButton("Электронные ресурсы")
        button4 = types.KeyboardButton("Общежития")
        button5 = types.KeyboardButton("Информация об онлайн-оплате")
        markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован..")


bot.polling(none_stop=True)
