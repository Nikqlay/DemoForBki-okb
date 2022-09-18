# В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

from ntpath import join


file = open('testSem4.txt', 'w', encoding='utf-8')
file.write('Мама сшила м0не штаны и7з бере9зовой кор45ы 893') 
file.close()

file = open('testSem4.txt', 'r', encoding='utf-8')
data = file.read().split()
result_text = []

for words in data:
    if words.isalpha():
        result_text.append(words)

file.close()
print(' '.join(result_text))


