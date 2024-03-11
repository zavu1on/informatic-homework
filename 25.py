with open('data/26-42.txt') as file:
    N, S = map(int, file.readline().split())
    arr = []
    for i in file.readlines():
        a, b, c = i.split()
        arr.append((a, int(b), int(c), int(b) * int(c)))

Z = list(filter(lambda el: el[0] == 'Z', arr))
Z.sort(key=lambda el: el[2])
Z.sort(key=lambda el: el[3])

for i in Z:
    if S - i[3] >= 0:
        S -= i[3]
    else:
        break

A = list(filter(lambda el: el[0] == 'A', arr))
A.sort(key=lambda el: el[2])
A.sort(key=lambda el: el[3])

count = 0
for i in A:
    if S - i[3] >= 0:
        S -= i[3]
        count += 1
    else:
        break

print(count, S)  # 202 9976
