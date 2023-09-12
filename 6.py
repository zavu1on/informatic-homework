from itertools import product

arr = product('САЛЬСА', repeat=6)

c = 0

for i in arr:
    if i.count('А') <= 1:
        c += 1

print(c)  # 16384
