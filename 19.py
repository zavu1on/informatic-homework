with open('data/17-7.txt') as file:
    f = [int(i) for i in file.readlines()]

count = 0
arr = []

for idx in range(len(f) - 2):
    a, b, c = f[idx:idx + 3]

    if a % 3 == 2 or b % 3 == 2 or c % 3 == 2:
        count += 1
        arr += [a, b, c]

s = 0
for _ in range(3):
    m = min(arr)
    s += m
    arr.remove(m)

print(count, s)  # 91 6