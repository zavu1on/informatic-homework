def f(n):
    s = str(n)

    s1 = 0
    s2 = 0

    for i in s:
        i = int(i)
        if i % 2 == 0:
            s1 += i

    for i in s[1::2]:
        s2 += int(i)

    return abs(s1 - s2)


for i in range(10 ** 6, 10 ** 7):
    if f(i) == 29:
        print(i)  # 6080818
        break
