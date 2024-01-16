with open('data/9-102.txt') as file:
    arr = file.readlines()

count = 0
for i in arr:
    a, b, c, d = sorted(map(int, i.split()))
    if a + b + c > d:
        count += 1

print(count)  # 4375