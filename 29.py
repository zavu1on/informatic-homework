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

            if count > 117:
                return count, m

    return count, m


i = 31

while i ** 2 <= 10 ** 9:
    i += 1
    s = str(i)

    if s[:2] != s[-2:]:
        continue

    count, m = f(i)

    if count == 117:
        print(i, m)

