def D(n, m):
    return n % m == 0


for A in range(1, 300):
    count = 0
    for x in range(1, 301):
        f = D(120, A) and ((D(x, 70) and D(x, 30)) <= D(x, A))

        if f:
            count += 1

    if count == 300:
        print(A)  # 30
