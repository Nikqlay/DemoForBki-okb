# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Enter digit " ))
def convert_decimall_binar(number):
    bin_number = ''
    while number > 0:
        bin_number += str(number % 2)
        number = number // 2
    return bin_number[::-1]
print(convert_decimall_binar(number))