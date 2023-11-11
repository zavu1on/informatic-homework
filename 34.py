def func(a, b):
    s = ''
    while a != 0:
        s += str(a % b)
        a //= b
    return s[::-1]


for i in range(2003, 2023 ** 3 * 10 + 1):
    s = str(i)
    f = False

    for idx, val in enumerate(s):
        try:
            if val == '2' and s[idx + 3] == '3':
                f = True
                break
        except IndexError:
            break

    if not f:
        continue

    a = func(i, 3)
    if a != a[::-1]:
        continue
    a = func(i, 9)
    if a != a[::-1]:
        continue
    a = func(i, 27)
    if a != a[::-1]:
        continue

    print(i, sum(map(int, oct(i)[2:])))