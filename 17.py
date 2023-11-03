resp = []
m = 0

for idx, i in enumerate(range(394480, 394541)):
    arr = [1, i]

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            arr.append(j)

            if i // j != j:
                arr.append(i // j)

    if len(arr) > m:
        resp = [(
            idx + 1, i, arr
        )]
        m = len(arr)
    elif len(arr) == m:
        resp += [(
            idx + 1, i, arr
        )]

resp.sort(key=lambda el: el[1])
for i in resp:
    print(i[1], i[0], len(i[2]), *sorted(i[2], reverse=True)[:2])