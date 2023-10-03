with open('data/k7-m1.txt') as file:
    f = file.read().strip()

s = f.replace('A', ' ').replace('B', ' ').split()
print(len(min(s)), len(s), len(f))  # 5 6 126