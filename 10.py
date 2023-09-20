from itertools import product

arr = product('0123456789ABCDEF', repeat=5)
c = 0

for i in arr:
    i = ''.join(i)

    if i[0] != 'F':
        continue
    if i[-1] != 'A':
        continue

    if i.count('3B') == 1:
        c += 1

print(c)  # 32