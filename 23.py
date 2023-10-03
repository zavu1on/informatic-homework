with open('data/k7a-3.txt') as file:
    f = file.read().strip()

f = f.replace('C', ' ').replace('D', ' ').split()
print(len(max(f, key=len)))  # 20