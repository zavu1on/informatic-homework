# 3 -> 20 -> 30

exclude = [12]
start = 3
end = 20
arr = [0] * 1000
arr[start] = 1

for i in range(start, end):
    if i in exclude:
        continue

    arr[i + 1] += arr[i]
    arr[i * 2] += arr[i]

a = arr[end]

start = 20
end = 30
arr = [0] * 1000
arr[start] = 1

for i in range(start, end):
    arr[i + 1] += arr[i]
    arr[i * 2] += arr[i]

b = arr[end]

print(a * b)  # 12