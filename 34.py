with open('data/17-1.txt') as file:
    f = [int(i) for i in file.readlines()]

count = 0
max_v = -10_000 * 3
mean = sum(f) / len(f)

for idx in range(len(f) - 2):
    a, b, c = sorted(f[idx:idx + 3])

    if a < mean and b < mean:
        if '6' in f'{a}{b}{c}':
            count += 1
            max_v = max(max_v, a + b + c)

print(count, max_v)  # 3617 8416


