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

arr.sort(key=lambda el: el[1], reverse=True)

for i in arr:
    if i[1] != arr[0][1]:
        break
    print(*i)

# 2 3
# 7 3
# 7 3
# 5 3
