def f(a):
    for x in range(1, 300):
        f = ((x & 7 != 0) <= ((x & a != 0) <= (x & 54 != 0))) <= ((x & 27 == 0) and (x & a != 0) and (x & 7 != 0))

        if f:
            return False
    return True


for a in range(1, 500):
    if f(a):
        print(a)

# 3