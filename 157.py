# 1 -> 600


def f(a, history, flag=False):
    if len(history) > 3 and sum(history[-3:]) % 11 == 0 and not flag:
        flag = True

    if a > 600:
        return 0
    if a == 600:
        if flag:
            return 1
        return 0

    return f(a + 2, [*history, a], flag) + f(a * 3, [*history, a], flag) + f(a * 4, [*history, a], flag)


print(f(1, []))  # 58046
