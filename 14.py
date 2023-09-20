from itertools import product

c1 = 0
c2 = 0
arr1 = product('0123456789', repeat=3)
arr2 = product('0123456789', repeat=2)

for i in arr1:
    if i[0] == '0':
        continue

    i = ''.join(i)

    if int(i[0]) ** 2 == int(i[1:]):
        c1 += 1

for i in arr2:
    i = ''.join(i)

    if int(i[1]) ** 3 == int(i[0]):
        c2 += 1

print(c1 * 100 * c2)  # 2700