def f(s):
    new = ''
    for i in s:
        if i == '0':
            new += '3'
        elif i == '1':
            new += '7'
        elif i == '2':
            new += '2'
        elif i == '3':
            new += '1'
        elif i == '4':
            new += '6'
        elif i == '5':
            new += '0'
        elif i == '6':
            new += '4'
        elif i == '7':
            new += '5'
    return new


n = '32006'
for _ in range(13):
    n = f(n)
print(n)  # 52774
