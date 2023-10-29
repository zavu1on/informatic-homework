with open('data/17-2.txt') as file:
    f = [int(i) for i in file.readlines()]

m = max(f)
p = f.index(m) + 1

print(f.count(m), p)  # 9 26
