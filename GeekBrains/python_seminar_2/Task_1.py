#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример: 6782 ->23
# 0.56 ->11

number = input('Enter a number: ')
sum_number = 0
for digit in number:
    if digit.isdigit():
        sum_number += int(digit)
    
print('Summa:', sum_number)        

  


