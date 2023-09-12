from itertools import product

arr = product('0123456', repeat=7)
c = 0

for i in arr:
    if i[0] in ['0', '3', '5']:
        continue

    i = ''.join(i)

    if '22' in i:
        continue
    if '44' in i:
        continue

    c += 1

print(c)  # 363416
