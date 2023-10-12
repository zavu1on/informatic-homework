with open('data/24-239.txt') as file:
    f = file.read().strip()

c = 0
m = 0

arr = []

for idx in range(len(f)):
    s1 = f[idx:idx + 2]
    s2 = f[idx:idx + 3]

    if s1 == 'XY':
        arr.append((idx, idx + 2))
    elif s2 == 'YZZ':
        arr.append((idx, idx + 3))
    elif s1 == 'YZ':
        arr.append((idx, idx + 2))

arr.append((len(f) + 10, len(f) + 11))

for idx in range(1, len(arr)):
    start = arr[idx - 1]
    end = arr[idx]

    if start[1] == end[0]:
        c += start[1] - start[0]
    else:
        c += start[1] - start[0]
        m = max(m, c)
        c = 0

m = max(m, c)

print(m)  # 314