mi = 10000 - 1
ma = 1000

for i in range(1000, 10000):
    if 3 ** 7 - 1 <= i <= 3 ** 8 - 1:
        if i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
            mi = min(mi, i)
            ma = max(ma, i)

print(mi, ma)  # 2186 6558
