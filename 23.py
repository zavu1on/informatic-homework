with open('data/17-10.txt') as file:
    f = [int(i) for i in file.readlines()]

count = 0
s = 0

for idx in range(len(f) - 2):
    a, b, c = sorted(f[idx:idx + 3])

    if c ** 2 == b ** 2 + a ** 2:
        count += 1
        s += c

print(count, s)  # 370 209813