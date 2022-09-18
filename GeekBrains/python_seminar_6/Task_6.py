# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def xbonacci (x, y):
    return [x **i for i in range(1, y+1)]
step = input('Введите шаг последовательности:\n')
xbon = input('Введите количество членов последовательности:\n')
print(xbonacci (int(step), int(xbon)))