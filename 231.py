def f(n):
    s = str(n)

    if int(s[0]) % 4 == 0:
        s = '9' + s[1:]
    if int(s[0]) % 2 == 0 and int(s[0]) % 4 != 0:
        s = '3' + s[1:]

    return int(s)


count = 0
for i in range(100000000):
    r = f(i)
    if str(r)[0] == '9' and oct(r)[-1] == '4':
        count += 1

print(count)  # бесконечое множество
