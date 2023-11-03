c = 0

for i in range(2, 20001):
    arr = [1]

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            arr.append(j)

            if i // j != j:
                arr.append(i // j)

    if sum(arr) > i:
        c += 1

print(c)  # 4953