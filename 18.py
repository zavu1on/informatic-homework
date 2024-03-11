def D(n, m):
    return n % m == 0


def f(A):
    for x in range(1, 300):
        r = ((D(x, 36) and D(x, 42)) <= D(x, A)) and (A * (A - 25) < 25 * (A + 200))

        if not r:
            return False

    return True


for A in range(1, 300):
    if f(A):
        print(A)  # 84
