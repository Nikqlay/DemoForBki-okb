control = True
while control:
    week_day = input('Enter a number from 1 to 7 - ')
    if week_day.isdigit():
        week_day = int (week_day)
        if week_day >= 1 and week_day <= 7:
            control = False
        else:
            print('Error, enter number again')
    else:
        print('Enter digit')   
if week_day == 6 or week_day == 7:
    print ('Weekend')
else:
    print('Working day')