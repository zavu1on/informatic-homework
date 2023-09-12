from itertools import product

arr = product('РЕЖИМДНО', repeat=6)
A = 'РЖМДН'
B = 'ЕИО'
c = 0

for i in arr:
    if len(set(i)) != len(i):
        continue

    if i[0] not in A:
        continue
    if i[1] not in B:
        continue
    if i[-1] not in B:
        continue

    c += 1

print(c)  # 1800
