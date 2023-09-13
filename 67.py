from itertools import product

arr = product('ЕГЭИНФ', repeat=6)
c = 0

for i in arr:
    if i[0] != 'Е':
        continue
    if i[-1] not in ['Э', 'И']:
        continue

    i = ''.join(i)

    if i.count('ФИ') < 2:
        continue

    if 'ЕГЭ' in i:
        continue

    c += 1

print(c)  # 14