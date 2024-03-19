with open('data/27-12a.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

mult_count = {2: 0, 3: 0, 6: 0}
count = 0

for idx, i in enumerate(arr):
    if i % 6 == 0:
        count += idx
        mult_count[6] += 1
    else:
        if i % 2 == 0:
            count += mult_count[3] + mult_count[6]
            mult_count[2] += 1
        elif i % 3 == 0:
            count += mult_count[2] + mult_count[6]
            mult_count[3] += 1
        else:
            count += mult_count[6]

print(count)  # 47

# ---------------------------------------------------
with open('data/27-12b.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

mult_count = {2: 0, 3: 0, 6: 0}
count = 0

for idx, i in enumerate(arr):
    if i % 6 == 0:
        count += idx
        mult_count[6] += 1
    else:
        if i % 2 == 0:
            count += mult_count[3] + mult_count[6]
            mult_count[2] += 1
        elif i % 3 == 0:
            count += mult_count[2] + mult_count[6]
            mult_count[3] += 1
        else:
            count += mult_count[6]

print(count)  # 745460178
