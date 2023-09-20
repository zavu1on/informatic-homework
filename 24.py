from itertools import product

arr = product('012345678', repeat=6)
c = 0

for i in arr:
    if i[0] == '0':
        continue

    if i.count('6') != 2:
        continue

    i2 = ''

    for j in i:
        if j == '6':
            i2 += '6'
        elif int(j) % 2 != 0:
            i2 += '0'
        else:
            i2 += '1'

    if '06' in i2 or '60' in i2:
        continue

    c += 1

print(c)  # 12224