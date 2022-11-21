# Напишите программу для
# проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
# ⋀ - and ⋁ - or ¬ - not

print("Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для следующих значений предикат соответственно: ")
for el in range(2):
    for el2 in range(2):
        for el3 in range(2):
            if (not (el or el2 or el3)) == ((not el) and (not el2) and (not el3)):
                print(el, el2, el3, sep=', ')
