with open('data/17-10.txt') as file:
    f = [int(i) for i in file.readlines()]

c = 0
m = 0


def to_7_base(n):
    res = ''
    while n != 0:
        res += str(n % 7)
        n //= 7

    return res[::-1]


for idx in range(len(f) - 1):
    a, b = f[idx:idx + 2]
    s = to_7_base(a + b)

    if s == s[::-1]:
        c += 1
        m = max(m, s, key=int)

print(c, m)  # 243 25552
