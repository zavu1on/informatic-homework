from collections import Counter
from string import ascii_uppercase

with open('data/24-164.txt') as file:
    f = file.read().strip()

arr = []

for i in f.split():
    x_count = i.count('X')
    letters_count = []

    for j in ascii_uppercase:
        letters_count.append(i.count(j))

    c = x_count - 1
    while c not in letters_count and c > 0:
        c -= 1

    if c <= 0:
        continue

    for idx in range(len(letters_count)):
        if letters_count[idx] == c:
            arr.append(ascii_uppercase[idx])

c = Counter(arr)
print(max(c.values()))  # 76

