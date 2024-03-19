with open('data/27-9a.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

tmp = None
R = float('inf')

for idx in range(6, len(arr)):
    b = arr[idx - 6]
    if b % 2 != 0:
        if not tmp:
            tmp = b
        else:
            tmp = min(tmp, b)

    a = arr[idx]
    if a % 2 != 0 and tmp:
        R = min(R, a * tmp)

print(R)  # 2465

# ------------------------------------------
with open('data/27-9b.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

tmp = None
R = float('inf')

for idx in range(6, len(arr)):
    b = arr[idx - 6]
    if b % 2 != 0:
        if not tmp:
            tmp = b
        else:
            tmp = min(tmp, b)

    a = arr[idx]
    if a % 2 != 0 and tmp:
        R = min(R, a * tmp)

print(R)  # 121
