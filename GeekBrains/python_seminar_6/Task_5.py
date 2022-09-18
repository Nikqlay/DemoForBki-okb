# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
import math


my_lst = [2, 3, 4, 5, 6]
print(my_lst)
def multip_pair_numbers(number):
  return [number[i] * number[-i-1] for i in range(math.ceil(len(number)/2))]

print(multip_pair_numbers(my_lst))