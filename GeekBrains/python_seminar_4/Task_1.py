# Вычислить число c заданной точностью d. 
# Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример:
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

# использование формулы Лейбница X = 4 - 4/3 + 4/5 - 4/7 + 4/9 - .....

denominator = 1 
summ = 0
for i in range(1000000):
    if i % 2 ==0:
        summ +=4 / denominator
    else:
        summ -= 4 / denominator
    denominator += 2
print (summ)

def set_accuracy(d:str):
    str_point = d.split('.')
    str_res = len(str_point[-1])
    return str_res

print(round(summ, set_accuracy('0.001')))

#print(format(summ, '.4'))  можно без функции так записать?