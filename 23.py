# 3 -> 12 -> 20

start = 3
end = 12
arr = [0] * 1000
arr[start] = 1

for i in range(start, end):
    arr[i + 1] += arr[i]
    arr[i + 3] += arr[i]

a = arr[end]

start = 12
end = 20
arr = [0] * 1000
arr[start] = 1

for i in range(start, end):
    arr[i + 1] += arr[i]
    arr[i + 3] += arr[i]

b = arr[end]

print(a * b)  # 247