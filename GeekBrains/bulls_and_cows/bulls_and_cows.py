from asyncore import dispatcher
from ntpath import join
from shutil import move
from turtle import update
import telebot
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import os
from config import TOKEN
import random
from random import randint, choice

game = False
count = 0
words = ['ночь', 'утро', 'заря', 'сало', 'мыло', 'жало', 'мозг', 'крот', 'соль', 'лось', 'кедр']
question= choice(words)

bot = telebot.TeleBot(TOKEN)
dispatcher = Updater.dispatcher

print("A'm is started")


def start(update, context):
    global game
    arg = context.args
    if not arg:
        #context.bot.send_message(chat_id, 
        context.bot.send_message(update.effrctive_chat_id, 
        'Привет! \n'
        'Игра Быки и коровы\n'
        'В ходе игры за несколько попыток игрок должен определить\n'
        'слово состоящее из четырех неповторяющихся букв.'
        'После каждой попытки бот сообщает количество угаданных букв\n'
        '«Корова» - буква присутствует в слове но находится не на своем месте\n'
        '«Бык» - буква присутствует в слове и находится на своем месте\n')
        game = True
    
def game(event):
    global count
    attempt = ans.get()
    bulls = 0
    cows = 0
    count += 1
    if attempt == question:
        print('Ты угадал, это', question)
        print('Количество попыток:', count)
        letter1['text'] = question[0]
        letter2['text'] = question[1]
        letter3['text'] = question[2]
        letter4['text'] = question[3]
        check.unbind('<Button-1>')
    else:
        if len(attempt) > 4 or len(set(attempt)) < 4:
            attempt = input('Нужно слово из 4 различных букв, '
                            'попробуй еще раз.\n')
        else:
            for i in range(4):
                if attempt[i] == question[i]:
                    bulls += 1
                elif attempt[i] in question:
                     cows += 1
        print(str(count), '.', 'Быки:', bulls, 'Коровы:', cows, attempt)


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    satates={
        PLAYER: [MessageHandler(Filters.text, plaer_name)],
        MOVE: [MessageHandler(Filters.text, step)]
    },
    fallbacks=[CommandHandler('start', start)]
)

dispatcher.add_handler(conv_handler)
Updater.start_polling
Updater.idle     