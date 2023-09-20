from itertools import permutations

arr = permutations('ОДЕКОЛОН')
c = 0
s = set()

for i in arr:
    for idx, val in enumerate(i):
        try:
            next = i[idx + 1]

            if val == next:
                break
        except IndexError:
            pass
    else:
        s.add(''.join(i))

print(len(s))  # 2400
