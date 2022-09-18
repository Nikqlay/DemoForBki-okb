# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:

# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# control = True       #хотелось добавить проверку на число, но не получилось, не знаю как с минусом быть. 
# while control:
#     coordinates_x = input('Enter coordinates x - ')
#     coordinates_y = input('Enter coordinates y - ')
#     if coordinates_x.isdigit() and coordinates_y.isdigit():
#         coordinates_x = int (coordinates_x)
#         coordinates_y = int (coordinates_y)
#         if coordinates_x == 0 and coordinates_y == 0:
#             control = False
#         else:
#             print('Error, enter coordinates again')
#     else:
#         print('Enter digit')   

coordinates_x = int (input('Enter coordinates x - '))
coordinates_y = int (input('Enter coordinates y - '))
while coordinates_x ==0 or coordinates_y == 0:
    print('Error, enter coordinates again')
    break

if coordinates_x > 0 and coordinates_y > 0:
    print ('Number of the quarter 1')
if coordinates_x < 0 and coordinates_y > 0:
    print ('Number of the quarter 2')
if coordinates_x < 0 and coordinates_y < 0:
    print ('Number of the quarter 3')  
if coordinates_x > 0 and coordinates_y < 0:
    print ('Number of the quarter 4')  