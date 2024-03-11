def D(n, m):
    return n % m == 0


def f(A):
    for x in range(1, 500):
        r = ((not D(x, A)) or D(x, 36) and D(x, 126)) and (A > 1000)

        if not r:
            return False

    return True


for A in range(1, 2000):
    if f(A):
        print(A)  # 1001
        break
