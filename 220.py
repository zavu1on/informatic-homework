def f(n):
    b = bin(n)[2:]

    s = 0
    for i in b:
        s += int(i)

    if s % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'

    return int(b, 2)


for i in range(1000):
    if f(i) < 35:
        print(i)  # 24
