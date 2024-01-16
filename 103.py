from math import sqrt, floor

with open('data/9-103.txt') as file:
    arr = file.readlines()

m = 0
for i in arr:
    a, b = map(int, i.split())
    m = max(m, sqrt(a ** 2 + b ** 2))

print(floor(m))  # 425