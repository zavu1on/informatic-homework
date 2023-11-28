# 2 -> 12 -> 34

start = 2
end = 12
arr = [0] * 1000
arr[start] = 1

for i in range(start, end):
    arr[i + 1] += arr[i]
    arr[i * 2] += arr[i]

a = arr[end]

start = 12
end = 33
arr = [0] * 1000
arr[start] = 1

for i in range(start, end):
    arr[i + 1] += arr[i]
    arr[i * 2] += arr[i]

b = arr[end]

print(a * b)  # 60