def f(a):
    for x in range(1, 300):
        f = ((x & 20 != 0) or (x & 55 != 0)) <= ((x & 7 == 0) <= (x & a != 0))

        if not f:
            return False
    return True


for a in range(100):
    if f(a):
        print(a)  # 48
        break