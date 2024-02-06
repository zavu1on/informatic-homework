def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += '10'
    else:
        b = '1' + b + '01'

    return int(b, 2)


for i in range(100):
    if f(i) > 420:
        print(i)  # 41
        break
