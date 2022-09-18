# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

list_number = [1.1, 1.2, 3.1, 5.567, 10.003]

def find_difference(list_number):
    value = [round(x - int(x), 3) for x in (list_number)]
    return max(value) - min(value)


print (list_number)
print(find_difference(list_number))