from itertools import product

arr = sorted(product('МАНГУСТ', repeat=6))

for idx, val in enumerate(arr):
    val = ''.join(val)
    idx = idx + 1

    if val[0] == 'У':
        continue
    if val.count('Г') > 1:
        continue
    if val.count('М') == 2:
        print(idx, val)  # 100810
