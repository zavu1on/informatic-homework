from collections import Counter

with open('data/9-221.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    i = list(map(int, i.split()))
    counter = Counter(i)
    v = sorted(counter.values(), reverse=True)

    if v[0] == 2 and set(v[1:]) == {1}:
        even = []
        odd = []

        for n in i:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        s1 = sum(even) if even else 0
        s2 = sum(odd) if odd else 0

        if s2 > s1:
            res += 1

print(res)  # 6