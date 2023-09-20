from itertools import product

arr = product('ЗЕРКАЛО', repeat=6)
c = 0

for i in arr:
    i = ''.join(i)

    if 1 <= i.count('К') <= 4:
        i2 = i.replace('К', '')

        if len(set(i2)) == len(i2):
            c += 1

print(c)  # 12570
