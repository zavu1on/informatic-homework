c = 0
m = 10001

for i in range(1000, 10002):
    if i % 10 == 0 or all([i % 63 == 0, i % 255 == 0]):
        c += 1
        m = min(i, m)

print(c, m)  # 902 1000
