with open('data/17-277.txt') as file:
    f = [int(i) for i in file.readlines()]

s = 0
count = 0
m = -1000 * 2
for i in f:
    if i % 60 == 0:
        i = abs(i)
        n_3 = ''
        while i != 0:
            n_3 += str(i % 3)
            i //= 3
        s += n_3.count('2') * 2

for idx in range(len(f) - 1):
    a, b = f[idx:idx + 2]

    if a > s or b > s:
        count += 1
        m = max(m, a + b)

print(count, m)  # 79 1909