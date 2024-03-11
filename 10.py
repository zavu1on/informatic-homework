def f(A):
    for x in range(1, 300):
        for y in range(1, 300):
            r = (x & 30 != 4) or ((x & 35 == 1) <= (x & A == 0))

            if not r:
                return False

    return True


for A in range(1, 300):
    if f(A):
        print(A)  # 2
        break
