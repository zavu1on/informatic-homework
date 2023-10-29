with open('data/17-243.txt') as file:
    f = [int(i) for i in file.readlines()]

max_n = 0
for i in f:
    if i % 133 == 0:
        max_n = max(max_n, i)

count = 0
min_s = 10_000 * 2

for idx in range(len(f) - 1):
    a, b = f[idx:idx + 2]

    if a > max_n or b > max_n:
        flag = False
        if '3' in oct(a):
            flag = True
        elif '3' in oct(b):
            flag = True

        if flag:
            count += 1
            min_s = min(min_s, a + b)

print(count, min_s)  # 34 11169
