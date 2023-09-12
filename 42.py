from itertools import product

arr = product('01234567', repeat=4)
c = 0

for i in arr:
    if i[0] == '0':
        continue

    if int(''.join(i), 8) % 4 == 0:
        c += 1

print(c)  # 896