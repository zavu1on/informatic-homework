def f(A):
    for x in range(1, 300):
        for y in range(1, 300):
            r = ((y - 20 < A) and (10 - x < A)) or (x * (y + 2) > 48)

            if not r:
                return False

    return True


for A in range(1, 300):
    if f(A):
        print(A)  # 27
        break
