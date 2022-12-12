# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3] (задание 3 семинар 4)


# было
# def Filter_unique(li):
#     li_two = list(set(li))
#     for el_1 in li_two:
#         if li.count(el_1) > 1:
#             li_two.remove(el_1)
#     return li_two


# li_one = [1, 1, 2, 3, 4, 4, 4]

# print(Filter_unique(li_one))

# стало

li_one = [1, 1, 2, 3, 4, 4, 4]
new_li = list(
    filter(lambda el: True if li_one.count(el) < 2 else False, li_one))
print(new_li)
