# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15] (задание 2 семинар 3)

from random import randint
from math import ceil #для округления до большего целого
# было
# list = []
# list_multiplication = []

# for i in range(1, random.randint(5, 10)):
#     list.append(i)

# i = 0
# j = -1

# while i < len(list)/2:
#     list_multiplication.append(int(list[i])*int(list[j]))
#     i += 1
#     j -= 1
# print(list, list_multiplication, sep=' => ')

# стало

li = [i for i in range(1, randint(5, 10))]

li_mult = list(map(lambda i: li[i]*li[-1-i], range(0, ceil(len(li)/2))))

print(li, li_mult, sep=' => ')
