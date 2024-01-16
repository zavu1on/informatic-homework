with open('data/9-202.txt') as file:
    arr = file.readlines()
    full = []
    for i in arr:
        full += i.split()

res = 0
for i in arr:
    i = i.split()

    if len(set(i)) == 6:
        for j in i:
            if full.count(j) == 11:
                res += 1
                break

print(res)  # 265