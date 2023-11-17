c = 0
i = 1_000_000 - 1


def f(n):
    resp = [1, n]

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            resp.append(i)

            if n // i != i:
                resp.append(n // i)

    return resp


while c < 6:
    i += 1

    arr = f(i)

    if len(arr) <= 40:
        continue

    if sum(arr) % 2 == 1 and 2 not in arr:
        print(i, len(arr))
        c += 1

"""
1071225 45
1147041 45
1334025 81
1432809 45
1625625 45
1656369 45
"""