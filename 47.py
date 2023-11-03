for i in range(78_000_000, 85_000_001):
    n = i

    if i ** 0.5 != int(i ** 0.5):
        continue

    arr = [1]

    if i % 2 != 0:
        arr.append(n)

    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            arr.append(j)

            if i // j != j:
                arr.append(i // j)

            if len(arr) > 5:
                break

    if len(arr) == 5:
        print(n, max(arr))
"""
78074896 1661168
80604484 1203052
82591744 1163264
"""