from itertools import product

arr = product('01234', repeat=5)
resp = 0

for i in arr:
    if i[0] == '0':
        continue

    c = 0

    for x in i:
        if int(x) % 2 == 0:
            c += 1

    if c <= 3:
        resp += 1

print(resp)  # 1744