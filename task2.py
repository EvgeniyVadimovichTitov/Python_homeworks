# Напишите программу, которая принимает на вход число
# N и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math
import random

n = random.randint(1, 10)
list_one_to_n = []

print(n)
for el in range(1, n+1):
    list_one_to_n.append(math.factorial(el))
print(list_one_to_n)
