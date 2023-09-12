from itertools import product

arr = product('012345678', repeat=7)
exclude_arr = [i * 3 for i in '012345678']
c = 0

for i in arr:
    if i[0] == '0':
        continue
    if i[-1] in ['3', '4', '7']:
        continue

    f = True
    i = ''.join(i)

    for x in exclude_arr:
        if x in i:
            f = False
            break

    if f:
        c += 1

print(c)  # 2676053