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


count = 0

for i in range(10000):
    r = f(i)
    if 500 <= r <= 700:
        count += 1

print(count)  # 20