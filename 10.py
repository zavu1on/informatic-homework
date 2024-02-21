for i in range(0, 9):
    s = '1' * i + '0' * (8 - i)
    n = int(s, 2)
    print((100 & n) == 0, s, n)