c = 0
m = 7752

for i in range(3721, 7752):
    s = sum(map(int, str(i)))

    if s % 3 == 0 and not bin(i)[2:].endswith('000'):
        c += 1
        m = min(i, m)

print(c, m)  # 1176 3723
