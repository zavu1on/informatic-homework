from itertools import product

arr = product('ХЛЕБНЫЙМЯКИШ', repeat=7)
c = 0

for i in arr:
    if i[0] != 'Х':
        continue

    f = False
    for j in 'БЫКИШ':
        if j in i:
            f = True
            break

    if not f:
        continue

    i2 = ''
    for j in i:
        if j in 'ХЛБНМКШ':
            i2 += '0'
        else:
            i2 += '1'

    if '00' in i2:
        continue

    c += 1

print(c)  # 336532