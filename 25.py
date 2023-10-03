with open('data/k7a-5.txt') as file:
    f = file.read().strip()

f = f.replace('C', ' ').replace('F', ' ').split()
print(len(max(f, key=len)))  # 19