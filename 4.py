from itertools import product

arr = sorted(product('АПРЕЛЬ', repeat=5), reverse=True)
c = 0

for idx, val in enumerate(arr):
    if idx == 387:
        break

    if val[-1] == 'Ь':
        c += 1

print(c)  # 65
