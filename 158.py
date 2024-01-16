with open('data/9-158.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    even = []
    odd = []

    for n in i.split():
        n = int(n)
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    s1 = sum(even) if even else 0
    s2 = sum(odd) if odd else 0

    if s2 > s1:
        res += 1

print(res)  # 1549