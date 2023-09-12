from itertools import product

arr = product('САКУРА', repeat=5)
c = 0

for i in arr:
    if i.count('А') <= 1:
        if i.count('У') <= 1:
            c += 1

print(c)  # 2538
