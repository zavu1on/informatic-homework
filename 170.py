from collections import Counter

with open('data/9-170.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    i = list(map(int, i.split()))
    counter = Counter(i)
    v = sorted(counter.values(), reverse=True)

    if v[0] == 2 and set(v[1:]) == {1}:
        items = sorted(counter.items(), key=lambda el: el[1], reverse=True)
        mean = 0
        for a, _ in items[1:]:
            mean += a
        mean /= 4

        if mean <= 2 * items[0][0]:
            res += 1

print(res)  # 2241