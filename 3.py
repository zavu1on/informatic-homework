from itertools import product

arr = product('01234567', repeat=4)
c = 0

for i in arr:
    if i[0] == '0' or int(i[0]) % 2 != 0:
        continue

    i = ''.join(i)
    if i == ''.join(sorted(i, reverse=True)):
        c += 1

print(c)  # 129