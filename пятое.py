import telebot
from telebot import types
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import webbrowser



# website - Открыть веб сайт
# site - Открыть веб сайт
# distiplini - Дисциплины 
# biblioteca - библиотеки
# document - документы
# dopobr - допалнительное образование


bot = telebot.TeleBot('7718775834:AAHxC_Ie9vspc-68sCM9Tb8U30kG74_HnD8')
# при нажатии на старт
@bot.message_handler(commands=['start', 'hello1'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

    bot.send_message(message.chat.id, 
                     "Привет, если вы хотите открыть веб сайт колледжа, выведите /site или /website ;"
                     "если вы хотите ознакомиться с библиотекой, введите /biblioteca ;"
                     "если хотите ознакомиться с документами по колледжу, то введите /document ;"
                     "если хотите увидеть ваши дисциплины, то введите /distiplini .")

# при нажати на библиотека
@bot.message_handler(commands=['biblioteca'])
def send_biblioteca(message):
    text = (
        "<b>Электронная библиотека</b>                                                                                     "
        "                                                             "
        "Каждый студент нашего учебного заведения имеет возможность бесплатно работать с лицензионной полнотекстовой базой электронных изданий Юрайт и Лань.                                                                                              "
        "В данной системе опубликованы надежные и полезные ресурсы, предназначенные для студентов разных специальностей, предоставляющие знания для успешной сдачи сессии, прохождения аттестации, написания научных трудов, подготовки проектов и последующей успешной работы."
    )

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Перейти в Лань", url="https://lanbook.com/")
    btn2 = types.InlineKeyboardButton("Перейти в Юрайт", url="https://urait.ru/")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=markup)

# при нажатии на сайт
@bot.message_handler(commands=['site', 'website'])
def site (message):
    webbrowser.open('https://open-college.ru/')

# при нажатии на доп
@bot.message_handler(commands=['dopobr'])
def site (message):
    webbrowser.open('https://open-college.ru/education/skills/')

groups_data = {
    "02.ЭиБУ.24.ОФ.О.2": ["<b>Математика</b> , Экзамен , Иванов Иван Иванович;", "<b>Физика</b> , Дифференцированный зачет , Петров Петр Петрович;", "<b>Информатика</b> , Экзамен , Сидоров Сидор Сидорович;"],
    "03.БД.24.ОФ.О.2": ["<b>Базы данных</b> , Экзамен , Смирнов Алексей Алексеевич;", "<b>Программирование</b> , Дифференцированный зачет , Кузнецов Дмитрий Дмитриевич;", "<b>Сети</b> , Экзамен , Васильев Василий Васильевич;"],
}

# при нажатии на дисциплины
@bot.message_handler(commands=['distiplini'])
def send_courses(message):
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 5):
        markup.add(types.InlineKeyboardButton(f"Курс {i}", callback_data=f"course_{i}"))
    bot.send_message(message.chat.id, "Выберите курс:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('course_'))
def send_groups(call):
    course = int(call.data.split('_')[1])
    groups = {
        1: ["02.ЭиБУ.24.ОФ.О.2", "03.БД.24.ОФ.О.2", "03.БД.24.ОФ.О.1", "04.СДО.24.ОФ.О.1", "05.ДО.24.ОФ.О.1"],
        2: ["01.ПиОСО.23.ОФ.О.2", "01.ПиОСО.23.ОФ.О.1", "03.БД.23.ОФ.О.1", "03.БД.23.ОФ.О.2", "04.СДО.23.ОФ.О.1"],
        3: ["15.ИСиП.22.ОФ.О.1", "15.ИСиП.22.ОФ.О.4", "15.ИСиП.22.ОФ.О.3", "15.ИСиП.22.ОФ.О.5", "15.ИСиП.22.ОФ.О.6"],
        4: ["04.СДО.21.ОФ.О.1", "05.ДО.21.ОФ.О.1", "06.КПвНО.21.ОФ.О.1", "06.КПвНО.21.ОФ.О.2", "06.КПвНО.22.ОФ.С.1"]
    }.get(course, [])
    markup = types.InlineKeyboardMarkup()
    for group in groups:
        markup.add(types.InlineKeyboardButton(group, callback_data=f"group_{group}"))
    bot.send_message(call.message.chat.id, "Выберите группу:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('group_'))
def send_subjects(call):
    group = call.data.split('_')[1]
    subjects = groups_data.get(group, [])
    bot.send_message(call.message.chat.id, "                                                                                                ".join(subjects), parse_mode='HTML')  

# при нажатии на документы
@bot.message_handler(commands=['document'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Бланки заявлений", callback_data='blanks')
    btn2 = types.InlineKeyboardButton("1Документы колледжа", callback_data='college')
    btn3 = types.InlineKeyboardButton("2Документы колледжа", callback_data='college1')
    btn4 = types.InlineKeyboardButton("3Документы колледжа", callback_data='college2')
    btn5 = types.InlineKeyboardButton("4Документы колледжа", callback_data='college3')

    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'blanks':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Гарантийное письмо_Мат. капитал", url='https://example.com/doc1')
        btn2 = types.InlineKeyboardButton("Заявление выход из АО", url='https://example.com/doc2')
        btn3 = types.InlineKeyboardButton("Заявление выход из АО", url='https://example.com/doc3')
        markup.add(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, "Выберите документ:", reply_markup=markup)
    elif call.data == 'college':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Выписка из реестра лицензий", url='https://example.com/doc4')
        btn2 = types.InlineKeyboardButton("Положение об очно-заочной и заочной формах обучения 2022 г", url='https://example.com/doc5')
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, "Выберите документ:", reply_markup=markup)
    elif call.data == 'college1':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Выписка из реестра лицензий", url='https://example.com/doc4')
        btn2 = types.InlineKeyboardButton("Положение об очно-заочной и заочной формах обучения 2022 г", url='https://example.com/doc5')
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, "Выберите документ:", reply_markup=markup)
       
    elif call.data == 'college2':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Выписка из реестра лицензий", url='https://example.com/doc4')
        btn2 = types.InlineKeyboardButton("Положение об очно-заочной и заочной формах обучения 2022 г", url='https://example.com/doc5')
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, "Выберите документ:", reply_markup=markup)
    elif call.data == 'college3':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Выписка из реестра лицензий", url='https://example.com/doc4')
        btn2 = types.InlineKeyboardButton("Положение об очно-заочной и заочной формах обучения 2022 г", url='https://example.com/doc5')
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, "Выберите документ:", reply_markup=markup)

bot.polling()