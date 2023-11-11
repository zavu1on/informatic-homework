from itertools import product


def f(n):
    res = 1
    m = 0

    two_count = 0
    while n % 2 == 0:
        if m == 0:
            m = n / 2

        n //= 2
        two_count += 1

    if two_count:
        res *= two_count + 1

    for i in range(3, n, 2):
        c = 0
        while n % i == 0:
            if m == 0:
                m = n / i

            n //= i
            c += 1
        if c:
            res *= c + 1

        if res > 12:
            return res, m
        if n == 1:
            return res, m

    return res, m


for i in range(3):
    arr = product('0123456789', repeat=i)
    for a in arr:
        s = int(f'12{"".join(a)}348')
        s_ = s

        if s ** 0.5 % 1 == 0 or s % 12 != 0:
            continue

        res, m = f(s)

        if res == 12:
            print(s, int(m))
"""
126348 63174
1203348 601674
1215348 607674
1242348 621174
1257348 628674
1266348 633174
1275348 637674
1287348 643674
"""