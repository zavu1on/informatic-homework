from itertools import product

arr = sorted(product('КОМПЬЮТЕР', repeat=5))

for idx, val in enumerate(arr):
    val = ''.join(val)
    idx = idx + 1

    if idx % 2 == 0:
        continue
    if val[0] == 'Ь':
        continue

    if val.count('К') == 2:
        print(idx, val)  # 58979