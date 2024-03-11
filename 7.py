with open('data/26-k4.txt') as file:
    N, K = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))

arr.sort(reverse=True)
a = arr[:K]
b = arr[K:2 * K]

print(sum(b) // len(b), sum(a) // len(a))  # 856 953
