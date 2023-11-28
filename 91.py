from itertools import product

arr = product('12', repeat=11)
resp = set()

for i in arr:
    n = 3
    for j in i:
        if j == '1':
            n += 1
        elif j == '2':
            n *= 2
            n += 1

    resp.add(n)

print(len(resp))  # 820
