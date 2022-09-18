import json
import controller
import check as ch

def create_json():
    json_data = []
    with open('db.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))

    controller.user_choice()

def add_to_json():
    user_id = ch.check_user_id()
    fist_name = ch.check_fist_name()
    last_name = ch.check_last_name()
    phone = ch.check_phone()
    comment = ch.check_comment()
    json_data = {
        "id": user_id,
        "first_name": fist_name,
        "last_name": last_name,
        "phone_number": phone,
        "comment": comment,
    }
    data = json.load(open('db.json'))
    data.append(json_data)
    with open('db.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        #json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nНовый контакт успешно добавлен!\n')
    controller.user_choice()
