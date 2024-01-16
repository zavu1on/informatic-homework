with open('data/9-160.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    a, b, c, d = sorted(map(int, i.split()))

    if d < a + b + c:
        if (a + d == b + c) or (a + b == c + d) or (a + c == d + b):
            res += 1

print(res)  # 35
