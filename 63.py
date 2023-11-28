from itertools import product

arr = product('123', repeat=7)
resp = set()

for i in arr:
    n = 1
    for j in i:
        if j == '1':
            n += 1
        elif j == '2':
            n += 5
        elif j == '3':
            n *= 3

    resp.add(n)

print(len(resp))  # 393
