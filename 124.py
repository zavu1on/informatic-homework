from itertools import permutations

arr = permutations('АМФИБРАХИЙ')
c = 0

for i in arr:
    i = ''.join(i)

    if i.startswith('АМ') and i.endswith('ИЙ'):
        c += 1

print(c)  # 2880

print(len(list(permutations('ФИБРАХ'))))  # 720
