from itertools import product

arr = sorted(product('ЛИСЁНОК', repeat=5))

for idx, val in enumerate(arr):
    if val.count('Ё') < 2:
        continue
    if val[0] == 'О':
        continue
    if val[1] == 'К':
        print(idx + 1, val)  # 15387