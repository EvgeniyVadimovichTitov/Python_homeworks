# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так:
#     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (задание 5 семинар 3)

# было
from random import randint


def Fibonachi(n):
    match n:
        case -1 | 1 | 2:
            return 1
        case 0:
            return 0
        case _:
            if n > 2:
                return Fibonachi(n-1)+Fibonachi(n-2)
            else:
                return Fibonachi(n+2)-Fibonachi(n+1)


# list_fibonachi = []
# n = randint(5, 9)
# print('Для числа', n, 'список:')
# for i in range(-n, n+1):
#     list_fibonachi.append(Fibonachi(i))
# print(list_fibonachi)

# стало

n = randint(5, 9)
print('Для числа', n, 'список:')
print(list(map(Fibonachi, [i for i in range(-n, n+1)])))
