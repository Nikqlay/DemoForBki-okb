#from .example import ai_player
import main
from random import randint


def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, '''
        Играем в конфеты. 
        Полиси: можно взять от 0 до 28 штук.
        Если взять меньше 0 (интересный вариант...) или больше 28,
        считается что взял 28. /Poehali.    
    '''
                                 )
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def game(update, context):
    main.game_on = True
    context.bot.send_message(update.effective_chat.id, "Игра началась. Выбери оппонента /Computer, /Human")
    person = randint(0, 1)
    if person == 0:
        context.bot.send_message(update.effective_chat.id, "Я хожу")
        return ai_player(main.candies)
    else:
        context.bot.send_message(update.effective_chat.id, "Ходи ты")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')