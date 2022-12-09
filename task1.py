# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

my_string = input('введите строку для корректировки: ')
correct_ch = input('введите символы для удаления слов, их содержащих: ')
string_correct = ''

for el in my_string.split():
    if correct_ch not in el:
        string_correct += el+' '

print(string_correct)
