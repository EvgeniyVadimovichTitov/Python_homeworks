# Напишите программу, которая принимает на вход цифру, обозначающую
# день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

week_day = int(input('Введите номер дня недели: '))

while 1:
    if (week_day > 7) or (week_day < 1):
        print('В неделе 7 дней введите значение от 1 до 7')
        week_day = int(input('Введите номер дня недели: '))
    elif (week_day == 6) or (week_day == 7):
        print('Выходной')
        break
    else:
        print('Будний')
        break