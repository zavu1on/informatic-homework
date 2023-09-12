from itertools import product

arr = product('ПИТОН', repeat=4)
c = 0

for i in arr:
    f = True

    for idx, val in enumerate(i):
        try:
            next = i[idx + 1]

            if val == next:
                f = False
                break
        except IndexError:
            pass

    if f:
        c += 1

print(c)  # 320