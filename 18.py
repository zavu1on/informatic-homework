from itertools import product

arr = product('КОМПЬЮТЕР', repeat=5)
c = 0

for i in arr:
    for j in 'КОТ':
        if j not in i:
            break
    else:
        c += 1

print(c)  # 3390
