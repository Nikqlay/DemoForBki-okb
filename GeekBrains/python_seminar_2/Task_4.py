# Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from timeit import default_timer as timer


def random_nimber():
    start_time = timer()
    number = str(start_time).split(".")
    print(f'{start_time}')
    random_digit = (int(number[0])^int(number[1]))
    print(random_digit)

random_nimber()