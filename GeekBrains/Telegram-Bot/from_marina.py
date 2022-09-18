import os
import telebot
import wikipedia
import re
import json
from config import TOKEN
from telebot import types
import functions as f
bot = telebot.TeleBot(TOKEN)

wikipedia.set_lang("ru")

markup = types.ReplyKeyboardMarkup(row_width=3)
button1 = types.KeyboardButton("Посмотреть список дел")
button2 = types.KeyboardButton("Создать задачу")
button3 = types.KeyboardButton("Очистить список дел")
button4 = types.KeyboardButton("Справка")
button5 = types.KeyboardButton("О программе")
button6 = types.KeyboardButton("Выйти")
markup.add(button1, button2, button3, button4, button5, button6)

if not os.path.exists('data.json'):
    f.write_to_file({})

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет! \n'
                              'Я твоя записная книжка,\n'
                              'мой функционал еще не идеален\n'
                              'но мы с командой к этому стремимся :)\n'
                              'Что можно сделать:\n'
                              '- Посмотреть список дел\n'
                              '- Создать задачу\n'
                              '- Удалить задачу\n'
                              '- Очистить список дел\n'
                              '- Получить справочную информацию\n'
                              '- Прочитать о программе и \n'
                              'узнать про моих создателей :)\n\n'
                              'В любой непонятной ситуации\n'
                              'пиши /start\n'
                              'и ты окажешься в главном меню!\n'
                              'а пока потыкай кнопки :)\n', reply_markup=markup)

@bot.message_handler()
def handle_message(msg):
    chat_id = str(msg.chat.id)

    # Список дел
    if msg.text == button1.text:
        json_data = f.read_from_file()
        todo_list = json_data.get(str(chat_id), [])
        if len(todo_list) == 0:
            bot.send_message(chat_id, 'Записная книжка пустая', reply_markup=markup)
            return

        todo_body = 'Список задач:\n'
        for i, j in enumerate(todo_list):
            todo_body += f'{i}) {j}\n'
        bot.send_message(chat_id, todo_body)

        list_markup = types.ReplyKeyboardMarkup(row_width=3)
        edit_button = types.KeyboardButton("Редактировать")
        completed_button = types.KeyboardButton("Выполнено")
        delete_button = types.KeyboardButton("Удалить")
        cancel_button = types.KeyboardButton("Назад")
        list_markup.add(edit_button, completed_button, delete_button, cancel_button)
        bot.send_message(chat_id, "Выберите действие",
                         reply_markup=list_markup)
    if msg.text == "Редактировать":
        bot.send_message(
            chat_id, 'Введите номер задачи которую необходимо отредактивароть')
        bot.register_next_step_handler(msg, edit_todo_from_list)
    ###
    if msg.text == "Выполнено":
        bot.send_message(chat_id, 'Введите номер задачи которая выполнена')
        bot.register_next_step_handler(msg, completed_todo_from_list)
    ###

    if msg.text == "Удалить":
        bot.send_message(
            chat_id, 'Введите номер задачи которую необходимо удалить')
        bot.register_next_step_handler(msg, delete_todo_from_list)

    if msg.text == "Назад":
        bot.send_message(
            chat_id, 'Возвращаемся в главное меню', reply_markup=markup)

    # Добавить задачу
    if msg.text == button2.text:
        bot.send_message(chat_id, 'Напишите, что добавить в список задач?')
        bot.register_next_step_handler(msg, add_todo_into_list)

    # Удалить все задачи
    if msg.text == button3.text:
        json_data = f.read_from_file()
        json_data[chat_id] = []
        f.write_to_file(json_data)
        bot.send_message(chat_id, 'Записная книжка очищена',
                         reply_markup=markup)

    # Справка
    if msg.text == button4.text:
        bot.send_message(chat_id, 'Какую справку хочешь получить?')
        bot.register_next_step_handler(msg, getwiki)

    # О программе
    if msg.text == button5.text:
        authors_list = f.all_authors()
        for i in range(len(authors_list)):
            bot.send_message(chat_id, authors_list[i])

    # Выход
    if msg.text == button6.text:
        bot.send_message(chat_id, 'До новых встреч!\n'
                                  'Соскучишься - жми')
        bot.send_message(msg.chat.id, '/start', reply_markup=types.ReplyKeyboardRemove())

def add_todo_into_list(message):
    chat_id = str(message.chat.id)
    json_data = f.read_from_file()
    user_todo = json_data.get(chat_id, [])
    user_todo.append(message.text)
    json_data[chat_id] = user_todo
    f.write_to_file(json_data)
    bot.send_message(chat_id, 'Задача добавлена', reply_markup=markup)

###
def completed_todo_from_list(message):
    chat_id = str(message.chat.id)
    json_data = f.read_from_file()
    user_todo = json_data.get(chat_id, [])
    try:
        todo_index = int(message.text)
    except ValueError:
        bot.send_message(chat_id, "Введи нормальное число!")
        return

    if todo_index < 0 or todo_index > len(user_todo):
        bot.send_message(chat_id, "Введи нормальное число! ")
        return

    def completed_todo(msg):
        # user_todo[todo_index] = msg.text
        user_todo[todo_index] = ('~'+user_todo[todo_index]+'~')
        json_data[chat_id] = user_todo
        f.write_to_file(json_data)
        bot.send_message(chat_id, "Я отметил задачу как выполненой", reply_markup=markup)

    bot.send_message(chat_id, '~'+str(user_todo)+'~', parse_mode='MarkdownV2')
    bot.register_next_step_handler(message, completed_todo)
###

def delete_todo_from_list(message):
    chat_id = str(message.chat.id)
    json_data = f.read_from_file()
    user_todo = json_data.get(chat_id, [])
    try:
        todo_index = int(message.text)
    except ValueError:
        bot.send_message(chat_id, 'Необходимо ввести число!')
        return

    if todo_index < 0 or todo_index > len(user_todo):
        bot.send_message(chat_id, 'Введи нормальное число!')
        return

    del user_todo[todo_index]
    json_data[chat_id] = user_todo
    f.write_to_file(json_data)
    bot.send_message(chat_id, 'Задача удалена')


def edit_todo_from_list(message):
    chat_id = str(message.chat.id)
    json_data = f.read_from_file()
    user_todo = json_data.get(chat_id, [])

    try:
        todo_index = int(message.text)
    except ValueError:
        bot.send_message(chat_id, "Введи нормальное число!")
        return

    if todo_index < 0 or todo_index > len(user_todo):
        bot.send_message(chat_id, "Введи нормальное число! ")
        return

    def edit_todo(msg):
        user_todo[todo_index] = msg.text
        json_data[chat_id] = user_todo
        f.write_to_file(json_data)
        bot.send_message(chat_id, "Я сохранил изменения", reply_markup=markup)

    bot.send_message(chat_id, 'Что будет в этой задаче?')
    bot.register_next_step_handler(message, edit_todo)

def getwiki(message):
    chat_id = str(message.chat.id)
    try:
        ny = wikipedia.page(message.text)
        # Получаем первую тысячу символов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip())) > 3):
                    wikitext2 = wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        bot.send_message(chat_id, wikitext2, reply_markup=markup)
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        bot.send_message(chat_id, 'В энциклопедии нет информации об этом', reply_markup=markup)

print('server started')
bot.polling()