for i in range(1000, 20001):
    arr = [1]

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            arr.append(j)

            if i // j != j:
                arr.append(i // j)

    if sum(arr) < i:
        print(i)