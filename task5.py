# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов
# (складываются числа, у которых "х" в одинаковых степенях).
# Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

import func

my_file = 'file.txt'

with open(my_file, 'r') as data:
    poly_1 = data.readline().rstrip('=0\n')
    poly_2 = data.readline().rstrip('=0\n')

with open(my_file, 'a') as data:
    data.write('\n')
    data.write('SUM')
    data.write('\n')
    data.writelines(func.List_to_string_poly(
        sorted(
            func.Sum_dict_poly(
                dict(map(
                    func.Parse_poly, func.Create_li_poly(
                        poly_1))), dict(map(
                            func.Parse_poly, func.Create_li_poly(
                                poly_2)))).items(), reverse=True)))
    data.write('=0')
