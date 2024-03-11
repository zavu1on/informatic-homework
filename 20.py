with open('data/26-k6.txt') as file:
    N, K = map(int, file.readline().split())
    arr = file.readlines()
arr = [tuple(map(int, i.split())) for i in arr]
# (вес, стоимость)

arr.sort(key=lambda el: -el[0])
arr.sort(key=lambda el: el[1])

a = arr[:K]
print(sum([i[0] for i in a]), max(a, key=lambda el: el[0])[1])  # 1567 248
