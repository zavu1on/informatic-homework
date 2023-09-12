from itertools import product

arr = product('СОТКАПЛЗ', repeat=5)
A = 'ОА'
c = 0

for i in arr:
    if len(i) != len(set(i)):
        continue

    if i[-1] in A:
        continue

    if 'ЗЛО' in ''.join(i):
        continue

    c += 1

print(c)  # 5008