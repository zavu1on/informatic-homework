from itertools import product

arr = product('ТИМАШЕВСК', repeat=6)
A = 'ИАЕ'
B = 'ТМШВСК'
c = 0

for i in arr:
    a = 0
    b = 0

    for x in A:
        a += i.count(x)
    for x in B:
        b += i.count(x)

    if a != b:
        continue

    sh = []
    for idx, val in enumerate(i):
        if val == 'Ш':
            sh.append(idx)

    f = True

    for sh_index in sh:
        if sh_index != 0:
            if i[sh_index - 1] in A:
                f = False
                break
        if sh_index != 5:
            if i[sh_index + 1] in A:
                f = False
                break

    if f:
        c += 1

print(c)  # 75870