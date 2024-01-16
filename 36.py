from math import floor

with open('data/9-J1.txt') as file:
    arr = []
    for i in file.readlines():
        i = i.replace(',', '.')
        arr += list(map(float, i.split()))

a1 = [i for i in arr if i < 0]
mean = floor(sum(a1) / len(a1))

print(mean, floor(max(arr)))  # -498 1000