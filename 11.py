def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'

    return int(b, 2)


arr = []
for i in range(100):
    r = f(i)
    if r > 116:
        arr.append(r)

print(arr)
print(min(arr))  # 120
