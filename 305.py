with open('data/24-1.txt') as file:
    f = file.read().strip()

a_idx = []
for idx, val in enumerate(f):
    if val == 'A':
        a_idx.append(idx)

m = 0
for idx, start in enumerate(a_idx):
    try:
        stop = a_idx[idx + 5]
        s = f[start:stop]

        m = max(m, len(s))
    except IndexError:
        pass

print(m)  # 213