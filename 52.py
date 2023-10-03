with open('data/k8-0.txt') as file:
    f = file.read().strip()

arr = []
tmp = ''

for i in f:
    if not tmp:
        tmp += i
    elif tmp and i == tmp[-1]:
        tmp += i
    else:
        arr.append((tmp[0], len(tmp)))
        tmp = i

print(*max(arr, key=lambda el: el[1]))  # 2 3