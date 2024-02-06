def f(n):
    b = bin(n)[2:]

    if n % 2 == 0:
        b = '1' + b + '10'
    else:
        b = '11' + b + '0'

    return int(b, 2)


arr = set()
for i in range(10000):
    r = f(i)
    if 800 <= r <= 1500:
        arr.add(r)

print(len(arr))  # 44