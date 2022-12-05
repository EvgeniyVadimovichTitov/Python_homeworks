# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

import random


def Find_num(n, i=2):
    li = []
    while n >= i:
        if not n % i:
            li.append(i)
            n = n/i
        else:
            i += 1
    return li


num = random.randint(1, 1000)

print(num, '=>', Find_num(num))
