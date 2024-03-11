with open('data/26-J4.txt') as file:
    N, = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))
arr.sort()

K = int(N * 0.1)
arr = arr[K:-K]

print(sum(arr), max(arr))  # 440962 91