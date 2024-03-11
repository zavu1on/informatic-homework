def f(A):
    for x in range(1, 300):
        for y in range(1, 300):
            r = (x > 4) or (x + 2 < y) or (x ** 2 + y ** 2 < A)

            if not r:
                return False

    return True


for A in range(1, 300):
    if f(A):
        print(A)  # 53
        break
