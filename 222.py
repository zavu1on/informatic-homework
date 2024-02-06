def f(n):
    s = str(n)

    if n % 2 == 0:
        s = sorted(s, reverse=True)
        n = int(''.join(s)) // 2
    else:
        s = sorted(s, reverse=True)
        n = int(''.join(s)) * 2

    return n


for i in range(10000):
    r = f(i)

    if r - 1 == i:
        print(r)  # 2
        break
