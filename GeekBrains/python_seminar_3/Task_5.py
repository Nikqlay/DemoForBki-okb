# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]   
#Негафибоначчи: F−1 = 1,   F−2 = -1,  Fn = F(n+2)−F(n+1). 
#Фибоначчи:  F_{0}=0,   F_{1} = 1, F_{n} = F_{n-1} + F_{n-2}



k = int(input("Enter digit "))
def nega_fibonacci(f):
    if f == -1:
        return 1
    if f == -2:
        return - 1
    if f != -1 and f != -2:
        return nega_fibonacci(f+2) - nega_fibonacci (f+1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-2) + fibonacci(n-1)    

lst_digit = []
for i in range(-k,0):
    lst_digit.append(nega_fibonacci(i))
for i in range(0, k+1):
    lst_digit.append(fibonacci(i))

print(lst_digit, '\n')




