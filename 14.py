with open('data/27-14a.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

ost = [0] * 12
count = 0

for i in arr:
    n = i % 12
    m = (12 - i) % 12

    count += ost[m]
    ost[n] += 1

print(count)  # 17

# ------------------------------------------
with open('data/27-14b.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

ost = [0] * 12
count = 0

for i in arr:
    n = i % 12
    m = (12 - i) % 12

    count += ost[m]
    ost[n] += 1

print(count)  # 150016535
