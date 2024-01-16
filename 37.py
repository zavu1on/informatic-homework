with open('data/9-J2.txt', encoding='utf8') as file:
    arr = [[i, 0] for i in range(34)]

    file.readline()
    i = file.readline()
    while i:
        i = i.replace(',', '.')

        _, *a = i.split()
        a = list(map(float, a))

        for idx, val in enumerate(a):
            arr[idx][1] += val

        i = file.readline()

    arr.sort(key=lambda el: el[1])

    print(arr[0][0], arr[-1][0])  # 31 7