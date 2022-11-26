# Реализуйте алгоритм перемешивания списка.

import random

numbers_one = []
numbers_two = []
number = random.randint(4, 8)


def Mix_list(my_list):  # перемешивание без оператора shuffle
    list_mix = []
    while len(my_list) > 0:
        temp = random.choice(my_list)
        list_mix.append(temp)
        my_list.remove(temp)
    return list_mix


for el in range(-number, number+1):
    numbers_one.append(el)
    numbers_two.append(el)


print(number)
print(numbers_one)
random.shuffle(numbers_one)
print(numbers_one)
print(Mix_list(numbers_two))
