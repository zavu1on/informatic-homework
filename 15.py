with open('data/27-15a.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

ost = [0] * 14
count = 0

for idx in range(5, len(arr)):
    b = arr[idx - 5]
    ost[b % 14] += 1

    a = arr[idx]
    j = (14 - a % 14) % 14
    count += ost[j]

print(count)  # 8

# -------------------------------------------
with open('data/27-15b.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

ost = [0] * 14
count = 0

for idx in range(5, len(arr)):
    b = arr[idx - 5]
    ost[b % 14] += 1

    a = arr[idx]
    j = (14 - a % 14) % 14
    count += ost[j]

print(count)  # 128567918
