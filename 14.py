resp = []
m = 0

for i in range(394441, 394506):
    arr = [1, i]

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            arr.append(j)

            if i // j != j:
                arr.append(i // j)

    if len(arr) > m:
        resp = [(
            i, arr
        )]
        m = len(arr)
    elif len(arr) == m:
        resp += [(
            i, arr
        )]

m = min(resp, key=lambda el: el[0])
print(len(m[1]), *sorted(m[1], reverse=True)[:2])
"""
48 394450 197225
"""
