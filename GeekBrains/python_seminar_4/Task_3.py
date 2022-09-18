# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]


number = int (input('Enter a number to decompose into prime factors: '))

def find_simple_multiplier(enter_number):
    divider = 2
    lst = []
    while enter_number > 0 and divider <= enter_number:
        if enter_number % divider == 0:
            lst.append(divider)
            enter_number = enter_number // divider
        else:
            divider +=1
    return lst

print('N =', number, '->', find_simple_multiplier(number))