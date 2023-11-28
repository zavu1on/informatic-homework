from itertools import product

# 2 -> 25

arr = product('123', repeat=7)
count = 0

for i in arr:
    n = 2
    for j in i:
        if j == '1':
            n += 1
        elif j == '2':
            n += 3
        elif j == '3':
            n *= 2

    if n == 25:
        count += 1

print(count)  # 53


def f(a, n=0):
    if a > 25 or n > 7:
        return 0
    if a == 25 and n == 7:
        return 1

    return f(a + 1, n + 1) + f(a * 2, n + 1) +f(a + 3, n + 1)


print(f(2))  # 53
