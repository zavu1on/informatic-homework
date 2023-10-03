with open('data/k7-44.txt') as file:
    f = file.read().strip()

f = f.replace('A', ' ').replace('B', ' ').split()
print(len(max(f)))  # 11