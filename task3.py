# Задайте список из n чисел последовательности
# (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

import math
import random

number = random.randint(1, 5)
list_seqence_to_n = []

print(number)
for el in range(1, number+1):
    list_seqence_to_n.append((1+1/el)**el)
print(list_seqence_to_n)
print('Сумма элементов последовательности равна:',
      round(math.fsum(list_seqence_to_n), 2))
