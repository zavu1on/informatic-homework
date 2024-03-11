with open('data/26-j7.txt') as file:
    N, = map(int, file.readline().split())
    arr = list(map(int, file.readlines()))
arr.sort()

a = arr[-int(N * 0.2):]
s1 = int(sum(a) * 0.8)
s2 = int(max(arr[:int(N * 0.8)]) * 0.6)

print(s1, s2)  # 143518 483