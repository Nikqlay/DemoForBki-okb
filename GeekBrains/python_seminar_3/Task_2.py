# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list_numbers = [2, 3, 4, 5, 6]
# def multip_pair_numbers(lst_num):

from random import randint

def get_numbers(n, first, last):
    return[randint(first, last) for i in range(n)]

n = 9
first = 1
last = 10

list_numbers = get_numbers(n, first,last)
print(list_numbers)

def multip_pair_numbers(number):
    result = []
    while len(number) > 1:
        result.append(number[0] * number[-1])
        del number[0]
        del number[-1]
    if len(number) ==1:
        result.append(number[0]**2)
    return result

print(multip_pair_numbers(list_numbers)) 