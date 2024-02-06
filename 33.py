def f(n):
    s = str(n)
    a = int(s[0]) + int(s[1])
    b = int(s[1]) + int(s[2])
    c = int(s[2]) + int(s[3])
    arr = [a, b, c]
    arr.remove(min(arr))

    return int(''.join(map(str, sorted(arr))))


resp = []
for i in range(1000, 10000):
    if f(i) == 1315:
        resp.append(i)

print(max(resp))  # 9676
