import json
import csv
import controller
import check as ch
import export
import user_interface as ui

from time import sleep
import subprocess
path_to_db = 'db.json'

def format_export():
    f_exp = ch.check_export()
    if f_exp == 1:
        export.json2txt()
    elif f_exp == 2:
        export.json2csv()
    elif f_exp == 3:
        controller.user_choice()
    else:
        print('Так мы еще не умеем')
        sleep(2)
        export.format_export()

def json2txt():
    with open(path_to_db) as json_file:
        data = json.load(json_file)
    json_obj = json.dumps(data, indent=2)
    output_dir = input(r'Укажите путь экспорта (Пример: c:\user_dir\txt\):''\n')
    output_file = input('Введите имя экспортируемого файла, с расширением (Пример: db.txt):\n')
    with open(output_dir + output_file, 'w') as f:
        f.write(json_obj)
    sleep(1)
    print(f'Файл {output_file}, успешно экспортирован в {output_dir}\n')
    sleep(2)
    open_folder = input('Открыть папку с экспортируемым файлом?\n'
                        '1: Да \n'
                        '2: Нет \n')
    if open_folder == '1':
        subprocess.Popen(fr'explorer {output_dir}')
        controller.user_choice()
    else:
        controller.user_choice()

def json2csv():
    with open(path_to_db) as json_file:
        json_obj = json.load(json_file)
    output_dir = input(r'Укажите путь экспорта (Пример: c:\user_dir\csv\):''\n')
    output_file = input('Введите имя экспортируемого файла, с расширением (Пример: db.csv):\n')
    data_file = open(output_dir + output_file, 'w', newline='')
    csv_writer = csv.writer(data_file)
    count = 0
    for data in json_obj:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close()
    print(f'Файл {output_file}, успешно экспортирован в {output_dir}\n')
    sleep(2)
    open_folder = input('Открыть папку с экспортируемым файлом?\n'
                        '1: Да \n'
                        '2: Нет \n')
    if open_folder == '1':
        subprocess.Popen(fr'explorer {output_dir}')
        controller.user_choice()
    else:
        controller.user_choice()

# user_dir = input(r'Укажите путь до файла (Пример: c:\user_dir\json\):''\n')
# user_file = input('Введите имя файла с расширением (Пример: db.json):\n')
#
