c = 0
m = 0


def gev_del(n):
    count = 2

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1

    return count


for i in range(1082, 129932):
    s = str(i)

    if ''.join(sorted(s, reverse=True)) == s and len(s) == len(set(s)):
        if gev_del(i) % 3 == 0:
            c += 1
            if s[0] == '7':
                m = max(m, i)

print(c, m)  # 121 76540
