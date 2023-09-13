from itertools import product

arr = product('ПОЛЯКВ', repeat=4)
s = 'ВОЛК'
resp = 0

for i in arr:
    c = 0

    for idx in range(4):
        if i[idx] == s[idx]:
            c += 1

    if c == 2:
        resp += 1

print(resp)  # 150