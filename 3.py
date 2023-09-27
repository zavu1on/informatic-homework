def f(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    return s


for n in range(35, 45):
    print(f('1' * n), n)  # 41