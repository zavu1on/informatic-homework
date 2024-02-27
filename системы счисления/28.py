def f(a):
    for x in range(1, 300):
        f = ((x & 56 != 0) or (x & 43 != 0)) <= (x & a != 0)

        if not f:
            return False
    return True


for a in range(75, 126):
    if f(a):
        print(a)  # 123
