with open('data/17-276.txt') as file:
    f = [int(i) for i in file.readlines()]

count = 0
m = 2

for idx in range(len(f) - 2):
    a, b, c = sorted(f[idx:idx + 3])

    if b ** 2 == a * c and a != b:
        count += 1
        m = max(m, c // b)

print(count, m ** 2)  # 8 1089