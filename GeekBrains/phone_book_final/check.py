import json
path_to_db = 'db.json'
def digit_check():
    while True:
        input_number = input('Введите число: \n')  # получаем строку
        try:
            input_number = int(input_number)  # пробуем перевести в число, если не удается переходим в except
            return input_number
        except:
            if input_number.isalpha():  # функция isalpha возвращает True если все символы буквы
                print("Введены буквы")
            else:
                print("Введены непонятные символа")
        return digit_check()


def check_user_id():
    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if len(data) == 0:
            user_id = 0
            print('Будет добавлена запись с id', user_id)
            return user_id
        else:
            for i in range(0, len(data)):
                item = data[i]
                user_id = int(item['id'])
    #        print('Последний id', user_id)
            user_id += 1
            print('Будет добавлена запись с id', user_id)
        return user_id

def check_fist_name():
    while True:
        fist_name = input('Введите имя: ')  # получаем строку
        try:
            if (len(fist_name) > 1 and len(fist_name) < 30) and fist_name !='': # проверяем длину строки, если не соответствует условию переходим в except
                #fist_name.capitalize()
                return fist_name.capitalize()
            else:
                print('Строка не должна быть менее 1 символа и более 30 \n'
                       'Строка не может быть пустой\n')
                continue

        except:
            # break
            print('Строка не должна быть менее 1 символа и более 30 \n'
                  'Строка не может быть пустой\n')

def check_last_name():
    while True:
        last_name = input('Введите фамилию: ')  # получаем строку
        try:
            if (len(last_name) > 1 and len(last_name) < 30) and last_name !='': # проверяем длину строки, если не соответствует условию переходим в except
                #last_name.capitalize()
                return last_name.capitalize()
            else:
                print('Строка не должна быть менее 1 символа и более 30 \n'
                      'Строка не может быть пустой\n')
                continue
        except:
            # break
            print('Строка не должна быть менее 1 символа и более 30 \n'
                  'Строка не может быть пустой\n')
def check_comment():
    while True:
        last_name = input('Введите комментарий: ')  # получаем строку
        try:
            if len(last_name) < 255: # проверяем длину строки, если не соответствует условию переходим в except
                last_name.capitalize()
                return last_name
            else:
                print('Строка не должна быть превышать 255 \n')
                continue
        except:
            break

def check_phone():
    while True:
        phone = input('Введите номер телефона: ')  # получаем строку
        try:
            n = int(phone)  # пробуем перевести в число, если не удается переходим в except
            return phone
            #break
        except:
            if phone.isalpha():  # функция isalpha возвращает True если все символы буквы
                print("Введены буквы")
            else:
                print("Введены непонятные символа")

def check_export():
    while True:
        f_exp = (input('В какой формат будем экспортировать?\n'
                               '1: TXT\n'
                               '2: CSV\n'
                               '3: Назад\n'))
        try:
            choice = int(f_exp)  # пробуем перевести в число, если не удается переходим в except
            return choice
        except:
            if f_exp.isalpha():  # функция isalpha возвращает True если все символы буквы
                print("Введены буквы")
            else:
                print("Введены непонятные символа")
        #return choice

def check_edit_data():
    while True:
        ch_edit = (input('Какие данные необходимо отредактировать?\n'
                               '1: Имя\n'
                               '2: Фамилию\n'
                               '3: Номер телефона\n'
                               '4: Комментарий\n'
                               '5: Назад\n'))
        try:
            choice = int(ch_edit)  # пробуем перевести в число, если не удается переходим в except
            return choice
        except:
            if ch_edit.isalpha():  # функция isalpha возвращает True если все символы буквы
                print("Введены буквы")
            else:
                print("Введены непонятные символа")
        #return choice