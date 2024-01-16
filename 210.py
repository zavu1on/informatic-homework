with open('data/9-210.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    a, b, c, d, e, f = sorted(map(int, i.split()))

    if f not in [a, b, c, d, e]:
        if len({a, b, c, d, e}) < 5:
            if f + a > sum([b, c, d, e]):
                res += 1

print(res)  # 22