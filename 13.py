def f(n):
    count = 2
    m = 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if m == 0:
                m = n // i

            count += 1

            if n // i != i:
                count += 1

            if count > 45:
                return count, m

    return count, m


i = 1000000004
c = 0
while c < 5:
    i += 100
    s = str(i)

    if not s.startswith('1') or '2' not in s or '7' not in s or not s.endswith('04'):
        continue

    s1 = s[s.find('2'):]
    if '7' not in s1:
        continue

    if i ** 0.5 % 1 != 0:
        continue

    res, m = f(i)
    if res == 45:
        print(i, m)
        c += 1

"""
1027330704 513665352
1132457104 566228552
1242703504 621351752
1271065104 635532552
1328748304 664374152
"""