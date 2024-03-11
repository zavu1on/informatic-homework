from math import ceil

with open('data/26-s1.txt') as file:
    N, = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))
arr.sort()

with_sale = [i for i in arr if i > 200]
sm = sum([i for i in arr if i <= 200])

K = len(with_sale) // 2
for idx, val in enumerate(with_sale):
    if idx + 1 <= K:
        sm += val * 0.1
    else:
        sm += val

print(ceil(sm))  # 365506
