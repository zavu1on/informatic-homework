with open('data/17-376.txt') as file:
    f = [int(i) for i in file.readlines()]

count = 0
m = '1'

for idx in range(len(f) - 2):
    a, b, c = f[idx:idx + 3]
    mul = a * b * c

    if mul <= 2 * 10 ** 9:
        mul = str(mul)

        if mul.startswith('53') and '7' in mul:
            count += 1
            m = max(m, mul, key=int)

print(count, m)  # 3 539750835