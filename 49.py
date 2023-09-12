from itertools import permutations

arr = permutations('АКАДЕМИК', 8)
A = 'АЕИ'
B = 'КДМК'
resp = set()

for i in arr:
    f = True

    for idx, val in enumerate(i):
        try:
            next = i[idx + 1]

            if val in A and next in A:
                f = False
                break
            if val in B and next in B:
                f = False
                break
        except IndexError:
            pass

    if f:
        i = ''.join(i)
        resp.add(i)

print(len(resp))  # 288
