from collections import Counter

with open('data/9-224.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    i = list(map(int, i.split()))
    counter = Counter(i)
    v = sorted(counter.values(), reverse=True)

    if v[0] == 2 and v[1] == 2 and set(v[2:]) == {1}:
        items = sorted(counter.items(), key=lambda el: el[1], reverse=True)
        n = items[-1][0]
        keys = sorted(counter.keys(), reverse=True)

        if keys[1] == n:
            res += 1

print(res)  # 2