# Найти расстояние между двумя точками пространства(числа вводятся через пробел)

def disstance (d: str):
    x1, y1, x2, y2  = list(map(int, d.split()))
    print('Расстояние между точками x1, y1=, x2=, y2=, Составляет:')
    disst = (((x2-x1)**2 + (y2-y1)**2)**0.5)
    return (disst)
coordinates = input('Введите координаты точек x1 y1 x2 y2 через пробел:')
print(disstance(coordinates))