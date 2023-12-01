# 1 -> 15 -> 43

exclude = [25, 30]


def f(start, stop):
    if start > stop or start in exclude:
        return 0
    if start == stop:
        return 1

    return f(start + 1, stop) + f(start + 2, stop) + f(start * 3, stop)


print(f(1, 15) * f(15, 43))  # 36753420

