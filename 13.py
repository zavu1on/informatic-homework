from itertools import product

arr = product('АБВГД', repeat=3)
c = 0

for i in arr:
    arr = [ord(x) for x in i]

    if arr == sorted(arr):
        c += 1

print(c)  # 35
