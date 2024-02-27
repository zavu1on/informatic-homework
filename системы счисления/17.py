def f(a):
    for x in range(1, 300):
        f = ((x & 30 == 0) or (x & 43 == 0)) <= ((x & 19 != 0) <= (x & a == 0))

        if not f:
            return False
    return True


for a in range(200):
    if f(a):
        print(a)  # 10
