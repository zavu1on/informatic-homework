from itertools import permutations

arr = permutations('АТТЕСТАТ', 8)
s = set()

for i in arr:
    i2 = ''
    for x in i:
        if x in 'ЕА':
            i2 += '0'
        else:
            i2 += '1'

    if '101' in i2:
        continue
    if '010' in i2:
        continue
    if i2.startswith('01') or i2.startswith('10'):
        continue
    if i2.endswith('01') or i2.endswith('10'):
        continue

    s.add(i)

print(len(s))  # 60