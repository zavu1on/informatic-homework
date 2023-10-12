with open('data/24-241.txt') as file:
    f = file.read().strip()

tmp = ''
m = 0

for i in f:
    if not tmp and i == 'O':
        tmp += i
    elif tmp and i == 'F' and tmp.count('F') == 2:
        tmp = ''
    elif tmp and i == 'O':
        m = max(len(tmp), m)
        tmp = i
    else:
        tmp += i

print(m)  # 47