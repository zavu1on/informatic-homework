def f(s):
    while '66' in s:
        s = s.replace('66', '1', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('22', '6', 1)

    return s


for i in range(50):
    print(f('6' * i), i)  # 48
