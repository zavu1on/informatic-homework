c = 0
ma = 123
mi = 1151


def gev_del(n):
    s = 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if n // i != i:
                s += n // i

    return s


for i in range(123, 1152):
    if i % 5 != 0:
        if gev_del(i) > 40:
            c += 1
            ma = max(ma, i)
            mi = min(mi, i)

print(c, ma - mi)  # 643 1026
