from itertools import product

arr = product('ОБЩЕСТВ', repeat=5)
c = 0

for i in arr:
    i = ''.join(i)

    if i[0] in 'ЩБ':
        continue
    if not i.endswith('ВВ'):
        continue
    if 'ЕВ' in i or 'ВЕ' in i:
        continue

    if 'ТБ' in i:
        c += 1

print(c)  # 11