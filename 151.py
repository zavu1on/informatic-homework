with open('data/9-150.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    a, b, c = sorted(map(int, i.split()))
    if a ** 3 > 3 * b * c:
        res += 1

print(res)  # 1644
