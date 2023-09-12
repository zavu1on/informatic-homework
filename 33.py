from itertools import product

arr = product('ПИКАЧУ', repeat=5)
c = 0

for i in arr:
    if i.count('У') >= 2:
        c += 1

print(c)  # 1526