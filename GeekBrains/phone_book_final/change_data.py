import json
import controller
import export
import check as ch
from time import sleep
path_to_db = 'db.json'

def change_user_data():
    ch_data = ch.check_edit_data()
    if ch_data == 1:
        change_first_name()
    elif ch_data == 2:
        change_last_name()
    elif ch_data == 3:
        change_phone_number()
    elif ch_data == 4:
        change_comment()
    elif ch_data == 5:
        controller.user_choice()
    else:
        print('Так мы еще не умеем')
        sleep(2)
        export.format_export()

def change_first_name():
    #####
    edit_id = input('Введите id записи, которую необходимо отредактировать:  ')
    id = int(edit_id)
    try:
        with open(path_to_db, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            for i in range(0, id + 1):
                if data[i]['id'] == id:
                    data[i]['first_name'] = input('Введите новое имя: ').capitalize()
        with open(path_to_db, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)
        print(f'\nИмя для запись с id {edit_id} успешно изменено!\n')
        #order_id()
        sleep(2)
        controller.user_choice()
    except:
        print(f'Записи с id {edit_id} не существует\n')
        sleep(2)
        controller.user_choice()
       ####

def change_last_name():
    #####
    edit_id = input('Введите id записи, которую необходимо отредактировать:  ')
    id = int(edit_id)
    try:
        with open(path_to_db, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            for i in range(0, id + 1):
                if data[i]['id'] == id:
                    data[i]['last_name'] = input('Введите новую фамилию: ').capitalize()
        with open(path_to_db, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)
        print(f'\nФамилья для запись с id {edit_id} успешно изменена!\n')
        #order_id()
        sleep(2)
        controller.user_choice()
    except:
        print(f'Записи с id {edit_id} не существует\n')
        sleep(2)
        controller.user_choice()
       ####



def change_phone_number():
    edit_id = input('Введите id записи, которую необходимо отредактировать:  ')
    id = int(edit_id)
    try:
        with open(path_to_db, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            for i in range(0, id + 1):
                if data[i]['id'] == id:
                    data[i]['phone_number'] = input('Введите новый номер телефона: ').capitalize()
        with open(path_to_db, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)
        print(f'\nНомер телефона для запись с id {edit_id} успешно изменен!\n')
        # order_id()
        sleep(2)
        controller.user_choice()
    except:
        print(f'Записи с id {edit_id} не существует\n')
        sleep(2)
        controller.user_choice()

def change_comment():
    #####
    edit_id = input('Введите id записи, которую необходимо отредактировать:  ')
    id = int(edit_id)
    try:
        with open(path_to_db, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            for i in range(0, id + 1):
                if data[i]['id'] == id:
                    data[i]['comment'] = input('Введите новыйы комментарий: ')
        with open(path_to_db, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)
        print(f'\nКомментарий для запись с id {edit_id} успешно изменен!\n')
        #order_id()
        sleep(2)
        controller.user_choice()
    except:
        print(f'Записи с id {edit_id} не существует\n')
        sleep(2)
        controller.user_choice()
       ####