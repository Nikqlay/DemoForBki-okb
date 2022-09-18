from tkinter import *
from tkinter import messagebox
import json
import user_interface as ui
import functions as f


window = Tk()
window.title('Мой список дел')
# window.geometry('350x300')
window.resizable(False, False)


start_dict = {}
temp_list = []
i = None

with open('data_file.json', 'r') as read_file:
    start_dict = json.load(read_file)

task_box = Listbox(selectmode=EXTENDED, font=('Aria Bold', 10))
task_box.grid(row=0, column=0, padx=15, columnspan=3, sticky=W+E)


def start(start_dict):
    if start_dict == {}:
        task_box.insert(END, 'Актуальных дел нет')
        # messagebox.showinfo('Приветствие',
        #             'Привет! Это твой список дел! Нажми на кнопку "Инструкция", чтобы посмотреть что я могу.')
        # После этой функуии не работает строка ввода данных
    else:
        for i in start_dict:
            task_box.insert(END, str(i) + ')' + start_dict[i])
    for i in start_dict:
        temp_list.append(i)


start(start_dict)
i = len(temp_list)+1


def add():
    global i
    task = task_entry.get()
    if task.strip():
        dict = {i: task}
        i += 1
        start_dict.update(dict)
        task_box.delete(0, i)
        task_entry.delete(0, END)
        start(start_dict)
    # elif task.isnumeric():
    #     print('Не вводите только числа') Проверка не работает(
    #     task_entry.delete(0, END)
    #     task_box.delete(0, i)
    #     start(start_dict)    
    else:
        messagebox.showwarning(
            "Предупреждение", "Нельзя оставить строку пустой!")
        task_box.delete(0, i)
        start(start_dict)


def del_all_data():
    global i
    task_box.delete(0, i)
    start_dict.clear()
    i = 1
    with open("data_file.json", "w") as write_file:
        json.dump(start_dict, write_file, indent=4)
    messagebox.showinfo("Ok", "Все дела успешно удалены")


def save():
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        json.dump(start_dict, write_file, indent=4)
    messagebox.showinfo("Ok", "Данные успешно сохранены")


def del_one_task():
    select = list(task_box.curselection())
    select.reverse()
    for i in select:
        task_box.delete(i)
    messagebox.showinfo('Молодец', 'Отлично! Одним делом меньше! \U0001f600')


def get_authors():
    msg = f.all_authors()
    task_box.delete(0, END)
    for i in range(len(msg)):
        task_box.insert(END, str(msg[i]))


task_label = ui.get_lable('Какое дело?:')
task_label.grid(row=1, column=0)

task_entry = ui.get_entry(window, 20)
task_entry.grid(row=1, column=1)

btn_add = ui.get_button('Добавить', add, 8)
btn_add.grid(row=1, column=2)

btn_del = ui.get_button('Удалить всё', del_all_data, 9)
btn_del.grid(row=3, column=0)

btn_save = ui.get_button('Сохранить', save, 8)
btn_save.grid(row=2, column=2)

btn_do_it = ui.get_button('Выполнить', del_one_task, 8)
btn_do_it.grid(row=3, column=2)

btn_get_aithors = ui.get_button('', get_authors, 1)
btn_get_aithors.grid(row=3, column=4)

btn_get_bugaga = ui.get_button('', f.easter_agg, 1)
btn_get_bugaga.grid(row=2, column=4)

btn_showinfo = ui.get_button('Инструкция', ui.get_info, 8)
btn_showinfo.grid(row=3, column=1)

window.mainloop()
