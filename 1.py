from itertools import product

arr = sorted(product('ЕПСУХ', repeat=5))
n = 1

for i in arr:
    i = ''.join(i)

    if i[-1] not in 'ПСХ':
        continue

    if i == 'УСПЕХ':
        print(n)  # 1293
        break

    n += 1

