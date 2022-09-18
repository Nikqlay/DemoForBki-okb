# Определить, присутствует ли в заданном списке строк, некоторое число
# Пример: Съ4ешь ещ1е этих мяг0ких фрунцу8зских булок178

from xml.dom.minidom import Element


my_text = 'Съ4ешь', 'ещ1е', 'этих', 'мяг0ких', 'фрунцу8зских', 'булок178'.split()
number = int(input('Enter number '))
def find_number(text, digit):
    return any(filter(lambda element: str(digit) in element, text))

print(find_number(my_text, number))





