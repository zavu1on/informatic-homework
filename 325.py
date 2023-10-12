with open('data/24-225.txt') as file:
    f = file.read().strip()

# FF44??78???3FF
m = 0

for idx in range(len(f)):
    s = f[idx:idx + 14]

    if s.startswith('FF44') and s.endswith('3FF'):
        n = s[2:-2]

        if n[4:6] == '78':
            m = max(m, int(n))

res = 0
for i in str(m):
    i = int(i)

    if i % 2 == 0:
        res += i

print(res)  # 38