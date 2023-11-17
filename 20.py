def f(n):
    count = 0
    m = 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if m == 0:
                m = n // i

            count += 1

            if n // i != i:
                count += 1

            if count > 7:
                return count, m

    return count, m


resp = []

for i in range(500_000_000, 100_000_000, -1):
    if i ** 0.5 % 1 != 0:
        continue

    count, m = f(i)

    if count == 7:
        resp.append((i, m))

        if len(resp) == 5:
            break

for i in resp[::-1]:
    print(*i)

"""
499164964 249582482
499343716 249671858
499656609 166552203
499701316 249850658
499835449 6327031
"""