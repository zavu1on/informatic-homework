with open('data/27-7a.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

R = 0
k = 0
d = 0

for i in arr:
    if i % 7 == 0 and i % 49 != 0:
        k = max(k, i)
    if i % 7 != 0:
        d = max(d, i)

R = k * d
print(R)  # 692286

# -----------------------------------------------
with open('data/27-7b.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

R = 0
k = 0
d = 0

for i in arr:
    if i % 7 == 0 and i % 49 != 0:
        k = max(k, i)
    if i % 7 != 0:
        d = max(d, i)

R = k * d
print(R)  # 952567
