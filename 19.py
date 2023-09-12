from itertools import product

arr = product('0123456789', repeat=6)
c = 0

for i in arr:
    if len(set(i)) != len(i) or i[0] == '0':
        continue

    f = True

    for idx, val in enumerate(i):
        try:
            val = int(val)
            next = int(i[idx + 1])

            if val % 2 == 0 and next % 2 == 0:
                f = False
                break
            if val % 2 != 0 and next % 2 != 0:
                f = False
                break
        except IndexError:
            pass

    if f:
        c += 1

print(c)  # 6480
