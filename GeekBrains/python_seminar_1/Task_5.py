# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

coordinates_x_A = float (input('Enter coordinates x point A - '))
coordinates_y_A = float (input('Enter coordinates y point A - '))
coordinates_x_B = float (input('Enter coordinates x point B - '))
coordinates_y_B = float (input('Enter coordinates y point B - '))
print(f'A ({coordinates_x_A}, {coordinates_y_A}); B ({coordinates_x_B}, {coordinates_y_B})')
distance_horizont = coordinates_x_B - coordinates_x_A
distance_vertical = coordinates_y_B - coordinates_y_A

result = round((distance_horizont**2 + distance_vertical**2)**0.5, 3)
print(result)



