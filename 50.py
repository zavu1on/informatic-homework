c = 0
m = 64354


def gev_del(n):
    count = 2

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1

    return count


for i in range(23561, 64355):
    if gev_del(i) > 20:
        c += 1
        m = min(m, i)

print(c, m)  # 5952 23562
