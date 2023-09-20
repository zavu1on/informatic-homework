from itertools import product

arr = product('АЕПСТУХ', repeat=7)
c = 0

for idx, val in enumerate(arr):
    val = ''.join(val)

    if idx < 999:
        continue

    for x in 'АЕПСТУХ':
        if x*2 in val:
            break
    else:
        c += 1

print(c)  # 326592