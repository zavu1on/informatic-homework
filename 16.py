m = 1000
c = 0

for i in range(1000, 10000):
    if i < 6 ** 5:
        if (i - 9) % 36 == 0 or (i - 10) % 36 == 0:
            c += 1
            m = max(m, i)

print(c, m)  # 376 7750
