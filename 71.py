def convert(a, base):
    r = ''
    while a:
        r += str(a % base)
        a //= base
    return r[::-1]


res = 0
for i in range(2, 11):
    s = convert(123, i)
    if list(s) == sorted(s):
        res += i

print(res)  # 26