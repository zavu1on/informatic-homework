count = 0


def f(a, n=0):
    global count

    if n > 9:
        return
    if a == 0 and n != 0:
        count += 1
        return

    return f(a + 3, n + 1), f(a - 1, n + 1)


f(0)
print(count) # 16
