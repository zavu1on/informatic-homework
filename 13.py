def f(A):
    for x in range(1, 300):
        for y in range(1, 300):
            r = (x & A != 0) and (x & 41 == 0) and (x & 37 == 0)

            if r:
                return False

    return True


for A in range(1, 300):
    if f(A):
        print(A)  # 45
