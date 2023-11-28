arr = set()


def f(a):
    if a >= 100:
        return

    if a % 2 == 0:
        arr.add(a)

    return f(a + 3), f(a * 3)

f(3)
print(len(arr))  # 16