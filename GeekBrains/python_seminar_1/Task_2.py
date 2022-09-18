#Напишите программу для проверки истинности утверждения ⌐(X V Y V Z) = ⌐X ∧ ⌐Y ∧ ⌐Z
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            left = not (x or y or z)
            right = not(x) and not(y) and not (z)
            print(f'{x} {y} {z} {left == right}')
