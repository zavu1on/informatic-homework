def f(a):
    for x in range(1, 300):
        f = (x & a == 0) <= ((x & 31 != 0) <= (x & 35 != 0))

        if not f:
            return False
    return True


for a in range(50, 121):
    if f(a):
        print(a)  # 60
