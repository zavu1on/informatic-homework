from itertools import product

arr = product('АЕЖЙМУ', repeat=5)
c = 0

for idx, val in enumerate(arr):
    if idx % 2 == 1:
        f = True

        for i, v in enumerate(val):
            try:
                n = val[i + 1]
                if n == v:
                    f = False
                    break
            except IndexError:
                pass

        if f:
            c += 1

print(c)  # 1875