from string import ascii_letters

with open('data/24-1.txt') as file:
    f = file.read().strip()

for i in ascii_letters:
    f = f.replace(i, ' ')
f = f.split()

m = float('-inf')

for i in f:
    i = int(i)

    if i % 2 == 0:
        m = max(m, i)

print(m)  # 54476