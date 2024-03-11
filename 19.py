with open('data/26-j8.txt') as file:
    N, = map(int, file.readline().split())
    arr = list(map(int, file.read().split()))
arr.sort()

a1 = arr[:int(N * 0.7)]
b1 = arr[-int(N * 0.3):]
s1 = int(sum(a1) * 0.7 + sum(b1) * 0.6)

a2 = arr[:int(N * 0.5)]
b2 = arr[int(N * 0.5):]
s2 = int(sum(a2) * 0.6 + sum(b2) * 0.65)

print(s1 - s2, int(max(b1) * 0.6))  # 63792 600
