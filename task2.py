# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
# в меню предусмотены игра против человека, против бота на рандоме, и бота с интелектом.
from random import randint


def Input_num(player: str):
    while True:
        try:
            num = int(
                input(f"{player}, введите количество конфет, которое возьмете от 1 до 28: "))
        except:
            print('Eror, введите число')
            continue
        if (num > 0) and (num < 29):
            return num
        print(f"{player}, введите корректное количество конфет: ")


def Print_result(player: str, num: int, count: int, candy: int):
    print(
        f"Ходил {player}, он взял {num}, теперь у него {count}. Осталось на столе {candy} конфет.")


def Clever_bot(candy: int):
    for num in range(28, 0, -1):
        if not ((candy-num) % 29):
            return num
    return randint(1, 28)


candy = 2021  # int(input('введите колличество конфет: '))
count_1 = 0
count_2 = 0
player_1 = ''
player_2 = 'Bot'
flag = randint(0, 1)
print(flag)

while True:
    try:
        command = int(
            input(
                '0 - 1vs1\n1 - одиночная игра\n2 - одиночная игра против гения\nВыберете режим игры: '))
    except:
        print('Eror, введите число')
        continue
    if (command > -1) and (command < 3):
        break
    else:
        print('Eror, недопустимая команда')

if (command == 1):
    player_1 = input('Введите имя игрока: ')
    if flag:
        print(f"Первый ходит {player_1}")
    else:
        print(f"Первый ходит {player_2}")
    while (candy > 28):
        if flag:
            n = Input_num(player_1)
            count_1 += n
            candy -= n
            flag = 0
            Print_result(player_1, n, count_1, candy)
        else:
            n = randint(1, 28)
            count_2 += n
            candy -= n
            flag = 1
            Print_result(player_2, n, count_2, candy)
elif (command == 2):
    player_1 = input('Введите имя игрока: ')
    if flag:
        print(f"Первый ходит {player_1}")
    else:
        print(f"Первый ходит {player_2}")
    while (candy > 28):
        if flag:
            n = Input_num(player_1)
            count_1 += n
            candy -= n
            flag = 0
            Print_result(player_1, n, count_1, candy)
        else:
            n = Clever_bot(candy)
            count_2 += n
            candy -= n
            flag = 1
            Print_result(player_2, n, count_2, candy)
else:
    player_1 = input('Введите имя 1-го игрока: ')
    player_2 = input('Введите имя 2-го игрока: ')

    if flag:
        print(f"Первый ходит {player_1}")
    else:
        print(f"Первый ходит {player_2}")
    while (candy > 28):
        if flag:
            n = Input_num(player_1)
            count_1 += n
            candy -= n
            flag = 0
            Print_result(player_1, n, count_1, candy)
        else:
            n = Input_num(player_2)
            count_2 += n
            candy -= n
            flag = 1
            Print_result(player_2, n, count_2, candy)
if flag:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл {player_2}")
