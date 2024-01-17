from collections import Counter

with open('data/9-226.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    i = list(map(int, i.split()))
    counter = Counter(i)
    v = sorted(counter.values(), reverse=True)

    if v[0] == 2 and v[1] == 2 and set(v[2:]) == {1}:
        m = max(i)
        if i.count(m) == 1:
            res += 1

print(res)  # 4