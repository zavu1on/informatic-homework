from itertools import permutations

arr = permutations('0123456789ABCEDF', 3)
c = 0

for i_ in arr:
    if i_[0] == '0':
        continue

    i = []
    for x in i_:
        if x == 'A':
            i.append(10)
        elif x == 'B':
            i.append(11)
        elif x == 'C':
            i.append(12)
        elif x == 'D':
            i.append(13)
        elif x == 'E':
            i.append(14)
        elif x == 'F':
            i.append(15)
        else:
            i.append(int(x))

    i_str = ''
    for x in i:
        if x % 2 == 0:
            i_str += '0'
        else:
            i_str += '1'

    if '00' in i_str or '11' in i_str:
        continue

    c += 1

print(c)  # 840
