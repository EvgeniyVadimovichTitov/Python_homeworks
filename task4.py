# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def Codding_rle(s: str):
    cod_str = ''
    cash_ch = ''
    count = 1
    if not s:
        return ''
    for char in s:
        if char != cash_ch:
            if cash_ch:
                cod_str += str(count)+cash_ch
                count = 1
            cash_ch = char
        else:
            count += 1
    else:
        cod_str += str(count)+cash_ch
    return cod_str


def Decodding_rle(s: str):
    dec_str = ''
    cash_count = ''
    for char in s:
        if char.isdigit():
            cash_count += char
        else:
            dec_str += char * int(cash_count)
            cash_count = ''
    return dec_str

#в файле предварительно нужен текст для кодировки или декодирования
my_command = int(input(
    '1 - кодировка из файла;\n2 - декодирование данных из файла;\nвведите команду: '))

file = 'text_for_task4.txt'
with open(file, 'r') as data:
    string_from_file = data.read()

print(string_from_file)

if (my_command == 1):
    with open(file, 'a') as data:
        data.write('\n')
        data.write('RLE codding:\n')
        data.write(Codding_rle(string_from_file))
elif (my_command == 2):
    with open(file, 'a') as data:
        data.write('\n')
        data.write('RLE decodding:\n')
        data.write(Decodding_rle(string_from_file))
else : print('EROR команда не коректна, перезапустите приложение')
