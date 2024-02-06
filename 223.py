def f(n, m):
    s_n = sum(map(int, bin(n)[2:])) ** 2
    s_m = sum(map(int, bin(m)[2:])) ** 2

    return s_n - s_m


arr = []
for n in range(500):
    for m in range(500):
        if f(n, m) == 33:
            arr.append(n + m)

print(min(arr))  # 142
