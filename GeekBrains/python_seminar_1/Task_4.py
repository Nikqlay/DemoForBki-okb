#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
control = True
while control:
    number_quarter = input('Enter a number quarter from 1 to 4 - ')
    if number_quarter.isdigit():
        number_quarter = int (number_quarter)
        if number_quarter > 0 and number_quarter <= 4:
            control = False
        else:
            print('Error, enter number again')
    else:
        print('Enter digit')   
if number_quarter == 1: 
    print ('x > 0, y > 0')
elif number_quarter == 2:
    print('x < 0, y > 0')
elif number_quarter == 3:
    print('x < 0; y < 0')
elif number_quarter == 4:
    print('x > 0; y < 0')

 