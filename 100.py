from math import gcd

with open('data/9-97.txt') as file:
    arr = file.readlines()

count = 0
for i in arr:
    a, b, c = sorted(map(int, i.split()))

    if c ** 2 == a ** 2 + b ** 2:
        if gcd(a, b) == gcd(a, c) == gcd(c, b) == 1:
            count += 1

print(count)  # 38