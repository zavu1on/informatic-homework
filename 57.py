from itertools import product
# 3 -> 27


def f(a, n=0):
    if a == 27 and n == 7:
        return 1
    if a > 27 or n > 7:
        return 0

    return f(a + 1, n + 1) + f(a + 4, n + 1) + f(a * 2, n + 1)


print(f(3))  # 37


arr = product('123', repeat=7)
count = 0

for i in arr:
    n = 3
    for j in i:
        if j == '1':
            n += 1
        elif j == '2':
            n += 4
        elif j == '3':
            n *= 2

    if n == 27:
        count += 1

print(count)  # 37