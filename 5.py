with open('data/26-k2.txt') as file:
    N, K = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))

arr.sort()
arr = arr[K:-K]
print(max(arr), sum(arr) // len(arr))  # 957 501
