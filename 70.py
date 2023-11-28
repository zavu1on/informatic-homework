def f(a, n=0):
    if a == 80 and n <= 5:
        return 1
    if a > 80 or n > 5:
        return 0

    return f(a + 1, n + 1) + f(a * 2, n + 1) + f(a + (a % 4), n + 1)


count = 0
for i in range(160):
    if f(i):
        count += 1

print(count)  # 34