with open('data/9-220.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    a, b, c, d = sorted(map(int, i.split()))

    if (a + d) % 3 == 0:
        if b - a == d - c:
            res += 1

print(res)  # 6