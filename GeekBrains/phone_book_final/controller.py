
import add_contact as ac
import user_interface as ui
import change_data as cud
#import change_phone_number as cpn
#import change_surname as cs
import delete_contact as dc
import view_all_contacts as vac
import export as exp


def user_choice():
    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 9:
        print('\nОшибка ввода!\n'
              '\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 1:
        ac.create_json()
    elif choice_num == 2:
        ac.add_to_json()
    elif choice_num == 3:
        cud.change_user_data()
    elif choice_num == 4:
        dc.delete_contact()
    elif choice_num == 5:
        vac.view_all_contacts()
    elif choice_num == 6:
        exp.format_export()
    elif choice_num == 0:
        print('\nСпасибо что воспользовались нашим приложением!\n'
              '\nДо новых встреч!')
        exit()
