with open('data/27-17a.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

count = 0
even_count = 0
odd_count = 0
even_13_count = 0
odd_13_count = 0

for idx in range(5, len(arr)):
    b = arr[idx - 5]
    if b % 13 != 0:
        if b % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    else:
        if b % 2 == 0:
            even_13_count += 1
        else:
            odd_13_count += 1

    a = arr[idx]
    if a % 13 == 0:
        if a % 2 == 0:
            count += odd_count
        else:
            count += even_count
    if a % 2 == 0:
        count += odd_13_count
    else:
        count += even_13_count

print(count)  # 6

# --------------------------------
with open('data/27-17b.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

# N = 7
# arr = [4, 14, 27, 39, 7, 2, 13]

count = 0
even_count = 0
odd_count = 0
even_13_count = 0
odd_13_count = 0

for idx in range(5, len(arr)):
    b = arr[idx - 5]
    if b % 13 != 0:
        if b % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    else:
        if b % 2 == 0:
            even_13_count += 1
        else:
            odd_13_count += 1

    a = arr[idx]
    if a % 13 == 0:
        if a % 2 == 0:
            count += odd_count
        else:
            count += even_count
    if a % 2 == 0:
        count += odd_13_count
    else:
        count += even_13_count

print(count)  # 129920689
