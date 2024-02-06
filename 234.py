def f(n):
    b = bin(n)[2:]

    if len(b) % 2 == 0:
        b += '10'
    else:
        b = '11' + b

    return int(b, 2)


resp = 0
for i in range(100, 201):
    if f(i) % 2 == 0:
        resp += 1

print(resp)  # 87
