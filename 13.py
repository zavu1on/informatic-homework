for i in range(78920, 92431):

    if i ** 0.5 != int(i ** 0.5):
        continue

    arr = [1, i]
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            arr.append(j)

            if i // j != j:
                arr.append(i // j)

    if len(arr) == 5:
        print(i, *sorted(arr))

"""
83521 1 17 289 4913 83521
"""