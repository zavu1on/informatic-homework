with open('data/k8-1.txt') as file:
    f = file.read().strip()

m = 0
tmp = ''

for i in f:
    if not tmp:
        tmp += i
    elif tmp and tmp[-1] != i:
        tmp += i
    else:
        m = max(len(tmp), m)
        tmp = i

print(m)
