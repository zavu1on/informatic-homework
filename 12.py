from itertools import permutations

arr = permutations('012345', 6)

for idx, val in enumerate(arr):
    val = ''.join(val)
    delta = abs(int(val) - int(val[::-1]))
    print(val)
    if delta == 15544:
        print(val, idx)
