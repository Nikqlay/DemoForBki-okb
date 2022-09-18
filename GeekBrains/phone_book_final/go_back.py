import controller
def go_back():
    g_b = input('Для возврата в главное меню нажмите q')
    if g_b == 'q':
        controller.user_choice()
