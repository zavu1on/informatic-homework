from itertools import permutations

arr = list(permutations(sorted('РУСЛАН')))

print(''.join(arr[441]))  # РСЛНУА