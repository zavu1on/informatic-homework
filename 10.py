for i in range(190061, 190081):
    n = i
    while i % 2 == 0:
        i //= 2

    if int(i ** 0.5) == i ** 0.5:
        continue

    arr = [1, i]
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            arr.extend([j, i // j])

            if len(arr) > 4:
                continue

    if len(arr) == 4:
        print(n, *sorted(arr, reverse=True))
"""
190061 190061 6131 31 1
190064 11879 1697 7 1
190067 190067 2677 71 1
190072 23759 1033 23 1
190073 190073 14621 13 1
190078 95039 13577 7 1
190079 190079 2837 67 1
"""
