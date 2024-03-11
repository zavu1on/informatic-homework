with open('data/26-J2.txt') as file:
    N = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))
arr.sort()

mean = sum(arr) / len(arr)
med = arr[len(arr) // 2 + 1]

res = 0
for i in arr:
    if mean <= i <= med:
        res += 1

print(res)  # 340