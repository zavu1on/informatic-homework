def f(n):
    s = str(n)
    a = int(s[0]) + int(s[1])
    b = int(s[2]) + int(s[1])

    return int(''.join(map(str, sorted([a, b], reverse=True))))


for i in range(100, 1000):
    if f(i) == 159:
        print(i)  # 187
        break
