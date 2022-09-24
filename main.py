import telebot
from telebot import types

bot = telebot.TeleBot('5634375605:AAETwJSyOylRX80MZKK8Tq_SxC48epUPlBs')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Информация о ВУЗе")
    btn2 = types.KeyboardButton("Задать вопрос напрямую")
    markup.add(btn1, btn2)
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
        btn4 = types.KeyboardButton("Приемная комиссия")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Выберите категорию".format(message.from_user), reply_markup=markup)
    elif message.text == "Бакалавриат":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Направления подготовки бакалавриата")
        btn2 = types.KeyboardButton("бак2")
        btn3 = types.KeyboardButton("бак3")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Задайте вопрос".format(message.from_user), reply_markup=markup)
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
        btn2 = types.KeyboardButton("маг2")
        btn3 = types.KeyboardButton("маг3")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Задайте вопрос".format(message.from_user), reply_markup=markup)
    elif message.text == "Направления подготовки магистратуры":
        markup = types.InlineKeyboardMarkup()
        mag1 = types.InlineKeyboardButton(text='Политология', url='http://imc-i.ru/magistratura/magisterskie-programmy/politologia/')
        mag2 = types.InlineKeyboardButton(text='Психология', url='http://imc-i.ru/magistratura/magisterskie-programmy/psixologiya/')
        mag3 = types.InlineKeyboardButton(text='Юриспруденция', url='http://imc-i.ru/magistratura/magisterskie-programmy/yuridicheskij/')
        mag4 = types.InlineKeyboardButton(text='Зарубежное регионоведение', url='http://imc-i.ru/magistratura/magisterskie-programmy/zarubezhnoe-regionovedenie/')
        mag5 = types.InlineKeyboardButton(text='Международные отношения', url='http://imc-i.ru/magistratura/magisterskie-programmy/mo/')
        mag6 = types.InlineKeyboardButton(text='Экономика', url='http://imc-i.ru/magistratura/magisterskie-programmy/economika/')
        mag7 = types.InlineKeyboardButton(text='Государственное и муниципальное управление', url='http://imc-i.ru/magistratura/magisterskie-programmy/gmu')
        mag8 = types.InlineKeyboardButton(text='Дизайн', url='http://imc-i.ru/magistratura/magisterskie-programmy/dizain/')
        mag9 = types.InlineKeyboardButton(text='Лингвистика', url='http://imc-i.ru/magistratura/magisterskie-programmy/lingvistika/')
        mag10 = types.InlineKeyboardButton(text='Журналистика', url='http://imc-i.ru/magistratura/magisterskie-programmy/zhurnalistika/')

        markup.add(mag1, mag2, mag3, mag4, mag5, mag6, mag7, mag8, mag9, mag10)
        bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
    elif message.text == "Аспирантура":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Направления подготовки аспирантуры")
        btn2 = types.KeyboardButton("асп2")
        btn3 = types.KeyboardButton("асп3")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Задайте вопрос".format(message.from_user), reply_markup=markup)
    elif message.text == "Направления подготовки аспирантуры":
        markup = types.InlineKeyboardMarkup()
        asp1 = types.InlineKeyboardButton(text='Психология труда, инженерная психология, когнитивная эргономика', url='http://imc-i.ru/psiholog/')
        asp2 = types.InlineKeyboardButton(text='Региональная и отраслевая экономика', url='http://imc-i.ru/economika/')
        asp3 = types.InlineKeyboardButton(text='Политические институты, процессы, технологии', url='http://imc-i.ru/politicheskie-nauki-i-regionovedenie/')

        markup.add(asp1, asp2, asp3)
        bot.send_message(message.chat.id, "Выберите направление", reply_markup=markup)
    elif message.text == "Приемная комиссия":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Адрес приемной комиссии")
        btn2 = types.KeyboardButton("Контакты приемной комиссии")
        btn3 = types.KeyboardButton("Время работы приемной комиссии")
        back = types.KeyboardButton("Вернуться в главное меню")

        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Задайте вопрос".format(message.from_user), reply_markup=markup)
    elif message.text == "Адрес приемной комиссии":
        bot.send_message(message.chat.id, text="г.Москва, Ленинский проспект, д.1/2, корп.1")
    elif message.text == "Контакты приемной комиссии":
        bot.send_message(message.chat.id, text="8 (800) 234-77-20 (звонок бесплатный), +7 (495) 632-17-70, +7 (916) "
                                               "393-00-55, +7 (916) 393-44-55, +7 (919) 998-89-72, +7 (919) 998-34-99")
    elif message.text == "Время работы приемной комиссии":
        bot.send_message(message.chat.id, text="Понедельник — пятница с 09:30 до 18:00 по МСК, суббота с 10:00 до "
                                               "18:00 по МСК.")
    elif message.text == "Задать вопрос напрямую":

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Информация о ВУЗе")
        button2 = types.KeyboardButton("Задать вопрос напрямую")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован..")


bot.polling(none_stop=True)
