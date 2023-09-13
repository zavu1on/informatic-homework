from itertools import product

arr = product('01234567', repeat=5)
c = 0

for i in arr:
    if i[0] == '0':
        continue

    if i.count('6') != 1:
        continue

    six_idx = i.index('6')
    if six_idx != 0:
        if int(i[six_idx - 1]) % 2 != 0:
            continue

    if six_idx != 4:
        if int(i[six_idx + 1]) % 2 != 0:
            continue

    c += 1

print(c)  # 2961