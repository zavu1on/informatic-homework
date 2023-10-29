with open('data/17-4.txt') as file:
    f = [int(i) for i in file.readlines()]

s = 0
c = 0

for i in f:
    if i % 16 == 11:
        if i % 7 == 0 and i % 6 != 0 and i % 13 != 0 and i % 19 != 0:
            s += i
            c += 1

print(s, c)  # 74452 12
