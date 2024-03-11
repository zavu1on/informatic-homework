with open('data/26-k5.txt') as file:
    N, K, M = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))
arr.sort()

cheap = arr[:K]
expensive = arr[-M:]

print(min(expensive), sum(cheap) // len(cheap))  # 27700 7896
