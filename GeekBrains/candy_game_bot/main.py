import telebot
from config import TOKEN
import random

bot = telebot.TeleBot(TOKEN)

candy = 0
first = None
user_id = 0

step = 28
min_candy = 10
max_candy = 500
game_over = False


@bot.message_handler(commands=['start'])
def new_game(message):
    global game_over
    global bot
    game_over = False
    global step
    global candy

    #
    candy = random.randint(min_candy, max_candy)

    first = random.randint(0, 1)
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id,
                     f"У нас {candy} конфет.\n"
                     f"Проиграит тот, кто заберет последнюю конфету.\n"
                     f"За один ход можно брать не более {step} конфет!"
                     )

    if first:
        bot.send_message(user_id, "Первым ходит игрок\n"
                                  "Сколько конфет хотите взять?")
    else:
        bot.send_message(user_id, f"Первым ходит бот")
        ai_move()


@bot.message_handler(func=lambda m: True)
def user_move(message):
    global game_over
    global step
    global candy
    global user_id
    global bot
    error = True
    if game_over:
        bot.send_message(
            user_id, f"Игра окончена.\n"
                     f"Чтобы начать новую нажмите\n"
                     f"/start")
    else:
        if step > candy:
            step = candy
        if message.text.isdigit():
            if int(message.text) > 0 and step + 1 > int(message.text):
                move = int(message.text)
                error = False
        if error:
            bot.send_message(
                user_id, f"Введите число от 1 до {step}")
            if message.text.isdigit and (int(message.text) > 0 and step + 1 > int(message.text)):
                move = int(message.text)
                error = False
        else:
            candy -= move
            win_combo()
            if game_over:
                bot.send_message(user_id, f"Игрок проиграл ((")
                bot.send_message(user_id, f"Ещё разок? \n"
                                          f"/start")
            else:
                ai_move()


def ai_move():
    global user_id
    global game_over
    global step
    global candy
    global bot
    bot.send_message(user_id, f"Осталось {candy} конфет")
    if step > candy:
        step = candy
    bot.send_message(
        user_id, f"Можно взять от одной до {step} конфет")
    if random.randint(0, 1):
        bot_move = random.randint(1, step)
    else:
        bot_move = candy % (step+1)
        if bot_move == 0:
            bot_move = random.randint(1, step)
    bot.send_message(user_id, f"Бот взял {bot_move} конфет")
    candy -= bot_move
    win_combo()
    if game_over:
        bot.send_message(user_id, f"Бот проиграл ((")
        bot.send_message(user_id, f"Ещё разок? /start!!!")
    else:
        if step > candy:
            step = candy
        bot.send_message(
            user_id, f"Осталось {candy} конфет.\nВозьмите от одной до {step} конфет")

def win_combo():
    global game_over
    if candy == 0:
        game_over = True


bot.infinity_polling()