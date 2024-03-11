with open('data/26-k3.txt') as file:
    N, K, M = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))

arr.sort(reverse=True)
a = arr[:K]
b = arr[K:M + K]

print(min(a), min(b))  # 909 519