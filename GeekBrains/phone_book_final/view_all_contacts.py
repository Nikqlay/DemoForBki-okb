import json
import controller
path_to_db = 'db.json'

def view_all_contacts():
    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    controller.user_choice()


