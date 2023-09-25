from itertools import product

arr = product('ПРОЛИВ', repeat=6)
c = 0

for i in arr:
    if 'П' in i:
        c += 1

print(c)  # 31031

print(1 * 6 * 6 * 6 * 6 * 6 * 5)  # 38880
