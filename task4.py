# Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# - -> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

import random

number = random.randint(4, 7)
list_numbers = []
multiplication = 1

for el in range(-number, number+1):
    list_numbers.append(el)
print(list_numbers)

el_index = input('введите индексы элементов одной строкой через пробел: ')

for el in el_index.split():
    if (el != ''):
        if (-2*number-2 < int(el) < 2*number+1):
            multiplication *= list_numbers[int(el)]
        else:
            print(f'элемента с индексом {el} не существует')
print(f'произведение указанных чисел равно: {multiplication}')
