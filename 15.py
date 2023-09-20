from itertools import product

arr = product('АНТИУОПЯ', repeat=6)
c = 0

for i in arr:
    if i[0] != 'А' and i[-1] != 'Я':
        c += 1

print(c * 7)