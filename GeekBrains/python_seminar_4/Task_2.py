#Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# original_list = [1, 2, 5, 8, 4, 2, 5, 3, 10, 8,]
original_list = list(map(int, input('Enter the numbers using a space:\n').split()))
print(original_list)

def find_unikum_elements(lst):
    result = []
    for i in lst:
        if not i in result:
            result.append(i)
    return result

unikum_elements = find_unikum_elements(original_list)

print(unikum_elements)
