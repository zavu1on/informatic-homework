with open('data/24-215.txt') as file:
    f = file.read().strip()

for i in 'ABC':
    f = f.replace(i, 'P')
for i in '123':
    f = f.replace(i, 'N')

print(f.count('NNP'))  # 18659