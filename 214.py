with open('data/9-214.txt') as file:
    arr = file.readlines()

res = 0
for i in arr:
    i = list(map(int, i.split()))
    if len(set(i)) == len(i):
        a, b, c, d, e = sorted(i)

        if c == (a + e) / 2 == (b + d) / 2:
            print(a, b, c, d, e)
            res += 1

print(res)  # 3
