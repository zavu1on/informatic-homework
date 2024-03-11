with open('data/26-J1.txt') as file:
    N = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))
arr.sort()

res = 0
for i in range(1, 51):
    a = arr.count(i)
    b = arr.count(100 - i)

    res += min(a, b)

    if i == 50:
        res += a // 2

print(res)  # 3915
