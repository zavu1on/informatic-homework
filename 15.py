with open('data/17-4.txt') as file:
    f = [int(i) for i in file.readlines()]

c = 0
m = 0

for i in f:
    if i % 5 == 3 and i % 9 == 5 and i % 8 != 7:
        c += 1
        m = max(m, i)

print(c, m)  # 43 9653