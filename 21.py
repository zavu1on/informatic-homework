def D(n, m):
    return n % m == 0


def f(A):
    for x in range(1, 500):
        r = (D(x, A) <= D(x, 54) or D(x, 130)) and (A > 110)

        if not r:
            return False

    return True


for A in range(1, 500):
    if f(A):
        print(A)  # 130
        break
