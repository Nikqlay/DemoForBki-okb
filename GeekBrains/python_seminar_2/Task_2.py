#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# Пример:
# Пусть N = 4, тогда [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial (number):
    mult = 1
    for i in range(number):
        mult *=i + 1
    return mult

enter_number = int (input('Enter number '))
result_num = [0] * enter_number
for i in range(enter_number):
    result_num[i] = factorial(i + 1)
 
print(f'Multiplication of numbers: \r\n{result_num}')

