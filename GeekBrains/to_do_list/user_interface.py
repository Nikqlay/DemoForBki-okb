from tkinter import *
from tkinter import messagebox


def get_button(name, to_do, size):
    button = Button(text=name, command=to_do,
                    font=('Arial Bold', 10), width=size)
    return button


def get_lable(name):
    label = Label(text=name, font=('Time New Roman', 13))
    return label


def get_entry(win, size):
    entry = Entry(win, width=size, font=('Arial Bold', 10))
    return entry

def get_info():
    return messagebox.showinfo('Инструкция','Для того, чтобы добавить дело, введи его\
    в поле ввода и нажми "Добавить". Спискок дел можно сохранить,\
    тогда при повторном запуке они загрузятся. Если списко дел\
    больше не нужен, его можно удалить полностью одним нажатием\
    кнопки "Удалить всё". Когда вы выполнили задачу, выделите её\
    курсором и нажмите "Выполнить". Выполненная задача\
    удалится из списка. Приятного использования! ')