with open('data/27-18a.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

count = 0
even_count = 0
odd_count = 0
even_13_count = 0
odd_13_count = 0

for idx in range(len(arr) - 2, len(arr) - 6, -1):
    b = arr[idx]
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

for idx in range(len(arr) - 1, 3, -1):
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

    if idx - 5 > 0:
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

        c = arr[idx - 1]
        if c % 13 != 0:
            if c % 2 == 0:
                even_count -= 1
            else:
                odd_count -= 1
        else:
            if c % 2 == 0:
                even_13_count -= 1
            else:
                odd_13_count -= 1

print(count)  # 11

# ----------------------------------------------------------------------
with open('data/27-18b.txt') as file:
    N = int(file.readline())
    arr = [int(i) for i in file.readlines()]

count = 0
even_count = 0
odd_count = 0
even_13_count = 0
odd_13_count = 0

for idx in range(len(arr) - 2, len(arr) - 6, -1):
    b = arr[idx]
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

for idx in range(len(arr) - 1, 3, -1):
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

    if idx - 5 > 0:
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

        c = arr[idx - 1]
        if c % 13 != 0:
            if c % 2 == 0:
                even_count -= 1
            else:
                odd_count -= 1
        else:
            if c % 2 == 0:
                even_13_count -= 1
            else:
                odd_13_count -= 1

print(count)  # 17813

