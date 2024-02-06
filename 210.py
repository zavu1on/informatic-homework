def f(n):
    b = bin(n)[2:]

    if n % 2 == 0:
        s = 0
        for i in b:
            s += int(i)
        s = bin(s)[2:]
        b += s
    else:
        b = '1' + b + '00'

    return int(b, 2)


for i in range(100):
    if f(i) > 215:
        print(i)  # 23
        break