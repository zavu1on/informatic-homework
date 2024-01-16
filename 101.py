with open('data/9-101.txt') as file:
    arr = file.readlines()

count = 0
for i in arr:
    a, b, c = sorted(map(int, i.split()))

    if (a == b and a != c) or (b == c and b != a):
        count += 1

print(count)  # 63