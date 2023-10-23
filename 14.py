m = 9482
s = 0

for i in range(1529, 9483):
    if (i - 1) % 4 == 0 and i % 5 == 3:
        m = min(m, i)
        s += i

print(m, s)  # 1533 2190194

m = 9482
s = 0

for i in range(1529, 9483):
    if i % 5 == 3:
        b = bin(i)
        if b.endswith('01'):
            m = min(m, i)
            s += i

print(m, s)

