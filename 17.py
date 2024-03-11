def f(A):
    for x in range(1, 300):
        for y in range(1, 300):
            r = ((x - 30 < A) and (15 - y < A)) or (x * (y + 3) > 60)

            if not r:
                return False

    return True


for A in range(1, 300):
    if f(A):
        print(A)  # 15
        break
