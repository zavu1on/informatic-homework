from itertools import product


def f(n: str):
    even = 0
    odd = 0

    for idx in range(len(n[::-1])):
        a = n[idx]
        if a == 'B':
            a = 9
        else:
            a = int(a)

        if idx % 2 == 0:
            even += a
        else:
            odd += a

    return int(''.join(map(str, sorted([even, odd], reverse=True))))


arr = product('12456B', repeat=4)
resp = []
for i in arr:
    i = ''.join(i)

    if f(i) == 115:
        resp.append((i, int(i, 12)))


print(max(resp, key=lambda el: el[1])[0])  # B421
