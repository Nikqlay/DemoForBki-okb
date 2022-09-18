# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

enter_number = int (input('Enter number '))
sum_number = 0
series_number = {}
for i in range(1, enter_number +1):
    series_number[i] = (1 +1/i) ** i
    sum_number += series_number[i]

print(f'Series number: \r\n {series_number}')
print(f'Sum of numbers: \r\n {sum_number}')




