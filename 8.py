with open('data/17-3.txt') as file:
    f = [int(i) for i in file.readlines()]

c = 0
m = -10_000 * 2

for idx in range(len(f) - 1):
    a, b = f[idx:idx + 2]

    if (a % 2) + (b % 2) == 1:
        if a % 2 == 0:
            even = a  # четный
            odd = b
        else:
            even = b
            odd = a

        if even % 4 == 0 and odd % 11 == 0:
            c += 1
            m = max(m, a + b)

print(c, m)  # 126 15701
