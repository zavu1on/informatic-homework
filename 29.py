with open('data/26-46.txt') as file:
    N, = map(int, file.readline().split())
    arr = [int(i) for i in file.readlines()]

count = 0
mn = float('inf')

for idx1 in range(len(arr)):
    a = arr[idx1]
    for idx2 in range(idx1 + 1):
        b = arr[idx2]
        for idx3 in range(idx2 + 1):
            c = arr[idx3]
            s = a + b + c

            if s % 3 == 0:
                mean = s // 3
                if mean in arr:
                    count += 1
                    mn = min(mn, mean)

print(count, mn)  # 536 10060497
