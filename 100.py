with open('data/24-2.txt') as file:
    f = file.read().strip()

arr = []
tmp = ''
m = 0

for i in f:
    if not tmp:
        tmp += i
    elif tmp and i > tmp[-1]:
        tmp += i
    else:
        m = max(m, len(tmp))
        arr.append(tmp)
        tmp = i

for i in arr:
    if len(i) == m:
        print(i)  # 3BEHUkvy
        break