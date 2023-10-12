with open('data/24-240.txt') as file:
    string = file.read().strip()

m = 0
tmp = ''
# DANOV
# 01234

for idx, val in enumerate(string):
    tmp += val

    end = string[idx - 4:idx+1]
    if not end:
        continue

    f = False

    if end.startswith('DANO'):
        f = True
    elif end[0] == 'D' and end[2:] == 'NOV':
        f = True
    elif end[:2] == 'DA' and end[3:] == 'OV':
        f = True
    elif end[:3] == 'DAN' and end[-1] == 'V':
        f = True
    elif end.endswith('ANOV'):
        f = True

    if end == 'DANOV':
        f = False

    if f:
        m = max(m, len(tmp) - 1)
        tmp = tmp[-4:]

print(m)  # 184293