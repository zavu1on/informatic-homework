with open('data/k7-m21.txt') as file:
    f = file.read().strip()

c = 0
res = 0

for idx in range(len(f) - 2):
    s = f[idx:idx + 3]

    if list(s) == sorted(s) and len(s) == len(set(s)):
        c += 1
        res = idx

print(c, res)  # 12 129
