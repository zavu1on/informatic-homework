from itertools import product

arr = sorted(product('УДАЧ', repeat=5))
n = 1

for val in arr:
    val = ''.join(val)

    if val[0] not in 'УА':
        continue

    if val == 'УДАЧА':
        print(n)  # 333

    n += 1

