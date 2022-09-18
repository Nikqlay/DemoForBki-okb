import json


def read_from_file() -> dict:
    with open('data.json', 'r') as f:
        json_data = json.load(f)
        return json_data


def write_to_file(json_data: dict):
    with open('data.json', 'w') as f:  # encoding='utf-8'
        json.dump(json_data, f)                     # ensure_ascii=False


def all_authors():
    messages = ['Над ботом работали объедененная команда студентов-энтузиастов GB: ', 'Антон Федонин', 'Андрей Полянский',
                'Татьяна Вальчик', 'Марина Ноздрачева', 'Александр Новиков', 'Эльмира Нургалеева']
    return messages
