# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import math

lst = []

for i in range(0, random.randint(5, 10)):
    lst.append(round(random.uniform(1, 11), 2))
print(lst, end=' =>\n')
lst = [round(val % 1, 2) for val in lst]
print(lst, end='=>')
print(round((max(lst) - min(lst)), 2))
