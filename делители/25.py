def D(n, m):
    return n % m == 0


for A in range(1, 300):
    count = 0
    for x in range(1, 301):
        f = D(190, A) and ((not D(x, A) and D(x, 15)) <= D(x, 75))

        if f:
            count += 1

    if count == 300:
        print(A)  # 5
