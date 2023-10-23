arr = []

for i in range(2020, 647039):
    i_str = str(i)
    s = sum(map(int, i_str))
    m = min(i_str)

    if s < 10 and m not in i_str[0:3]:
        arr.append(i)

mean = sum(arr) / len(arr)
N = 2020

for i in arr:
    if abs(mean - i) < abs(mean - N):
        N = i

print(len(arr), N)  # 1248 151000