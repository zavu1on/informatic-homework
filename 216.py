with open('data/9-215.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    a, b, c, d = sorted(map(int, i.split()))

    if b * c % a == 0:
        res += 1

print(res)  # 148