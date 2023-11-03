for idx, i in enumerate(range(194441, 196501)):
    if i ** 0.5 != int(i ** 0.5):
        continue

    arr = [1, i]

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            arr.append(j)

            if i // j != j:
                arr.append(i // j)

    print(idx + 1, i, len(arr), int(i ** 0.5))
"""
41 194481 25 441
924 195364 27 442
1809 196249 3 443
"""