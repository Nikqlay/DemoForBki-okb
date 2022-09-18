#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

number_lst = [2, 3, 5, 9, 3]

def sum_odd_position(num_lst):
    sum_elements = 0
    for i in range(1, len(num_lst), 2):
        sum_elements += num_lst[i]
        
    return sum_elements
        
print('\n', (number_lst), '- > сумма элементов, стоящих на нечетных позициях ',  sum_odd_position(number_lst))



