from collections import Counter

with open('data/9-227.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    i = list(map(int, i.split()))
    counter = Counter(i)
    v = sorted(counter.values(), reverse=True)

    if v[0] == 2 and set(v[1:]) == {1}:
        a, b, c, d = sorted(i)
        if c + d > (a + b) * 2:
            if d % a != 0:
                res += 1

print(res)  # 125