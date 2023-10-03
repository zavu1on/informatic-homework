with open('data/k7b-3.txt') as file:
    f = file.read().strip()

tmp = ''
m = 0

for i in f:
    if not tmp and i == 'B':
        tmp += i
    elif tmp and i in 'BAFE':
        if tmp[-1] == 'B' and i == 'A':
            tmp += i
        elif tmp[-1] == 'A' and i == 'F':
            tmp += i
        elif tmp[-1] == 'F' and i == 'E':
            tmp += i
        elif tmp[-1] == 'E' and i == 'B':
            tmp += i
        else:
            m = max(m, len(tmp))
            tmp = ''
    else:
        m = max(m, len(tmp))
        tmp = ''

print(m)  # 31

f = f.replace('BAFE', '4')
f = f.replace('4B', '5')
f = f.replace('5A', '6')
f = f.replace('6F', '7')

for i in 'ABCDEF':
    f = f.replace(i, ' ')

arr = []
for i in f.split():
    s = 0
    for j in i:
        s += int(j)

    arr.append(s)

print(max(arr))
