def f(n):
    o = oct(n)[2:]

    if n % 2 == 0:
        o += 'F'
    else:
        o += '0'

    s = 0
    for i in o:
        s += int(i, 16)
    o += oct(s % 16)[2:]

    s = 0
    for i in o:
        s += int(i, 16)
    o += oct(s % 16)[2:]

    return o


for i in range(1, 10000):
    r = f(i)
    a = max(r, key=lambda el: int(el, 16))
    b = min(r, key=lambda el: int(el, 16))
    if r.count(a) * 5 == r.count(b):
        print(i)  # 512
        break

