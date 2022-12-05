# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов(значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.

# Пример:

# - k = 2 = > 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k = 4 = > 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random
k_1 = random.randint(1, 9)
k_2 = random.randint(1, 9)


def Create_equation(n):
    li = list()
    for i in range(n, -1, -1):
        m = random.randint(-15, 15)
        if (not m):
            continue
        elif (not i):
            li.append(str(m))
        elif (m == 1 or m == -1):
            if (i == 1):
                li.append('x')
            else:
                li.append('x^'+str(i))
        elif (i == 1):
            li.append(str(m)+'x')
        else:
            li.append(str(m)+'x^'+str(i))
    for i in range(1, len(li)):
        if (li[i][0] != '-'):
            li[i] = "+" + li[i]
    li.append('=0')
    if (len(li) == 2) and ('x' not in li[-2]):
        li[-2] += 'x' + str(random.randint(1, 9))
    return li


my_li = Create_equation(k_1)
print(my_li)
my_li2 = Create_equation(k_2)
print(my_li2)

my_file = 'file.txt'
with open(my_file, 'w') as data:
    data.writelines(my_li)
    data.write('\n')
    data.writelines(my_li2)
