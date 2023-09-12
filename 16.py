from itertools import product

arr = product('0123456789ABCDEF', repeat=5)
c = 0

for i in arr:
    if sorted(i) == list(i) and i[0] != '0':
        print(i)
        c += 1

print(c)  # 11628