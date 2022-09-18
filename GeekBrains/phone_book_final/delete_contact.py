import json
import controller
from time import sleep
path_to_db = 'db.json'

def delete_contact():

    del_id = input('Введите id записи, которую необходимо удалить:\n'
                   'или нажмите q чтобы вернуться назад  ')
    if del_id == 'q':
        controller.user_choice()
    else:
        id = int(del_id)
        try:
            with open(path_to_db, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                for i in range(0, id + 1):
                    if data[i]['id'] == id:
                        del data[i]
            with open(path_to_db, 'w', encoding='UTF-8') as file:
                json.dump(data, file, indent=4)
            print(f'\nЗапись с id {del_id} успешно удалёна!\n')
            order_id()
            sleep(2)
            controller.user_choice()
        except:
            print(f'Записи с id {del_id} не существует\n')
            sleep(2)
            controller.user_choice()

def order_id():
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
             data[i]['id'] = i
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('id упорядочены!!\n')
    sleep(1)