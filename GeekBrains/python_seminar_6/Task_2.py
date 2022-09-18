#Найти сумму чисел списка стоящих на нечетной позиции
from functools import reduce


my_lst = [1,2,3,4,5]
def sum_lst(number):
    return sum(number [1::2])
print(sum_lst(my_lst))
