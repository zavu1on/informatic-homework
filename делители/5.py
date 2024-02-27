def D(n, m):
    return n % m == 0


for A in range(1, 300):
    count = 0
    for x in range(1, 301):
        f = (D(x, A) and not D(x, 15)) <= (D(x, 18) and D(x, 15))

        if f:
            count += 1

    if count == 300:
        print(A)  # 15
        break
