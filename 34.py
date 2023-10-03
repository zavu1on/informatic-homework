with open('data/k7c-2.txt') as file:
    f = file.read().strip()

c = 0

for idx in range(len(f) - 2):
    s = f[idx:idx + 3]

    if s[0] not in 'ACE':
        continue
    if s[1] not in 'ADF' or s[0] == s[1]:
        continue
    if s[2] not in 'ABF' or s[1] == s[2]:
        continue

    c += 1

print(c)  # 891