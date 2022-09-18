# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

my_lst = "qwe", "asd", "zxc", "qwe", "ertqwe"
find_word = "qwe" 
def second_enter(lst: list, num: int):
    return[i for i, element in enumerate(lst) if num in element] [1] if len(lst) > 2 else 0

print(second_enter(my_lst, find_word))