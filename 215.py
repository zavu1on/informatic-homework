def f(n):
    b = bin(n)[2:]

    if n % 2 == 0:
        b = '1' + b + '11'
    else:
        b = '11' + b + '0'

    return int(b, 2)


count = 0
for i in range(10000):
    if 500 <= f(i) <= 1000:
        count += 1

print(count)  # 59