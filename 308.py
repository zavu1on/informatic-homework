with open('data/24-208.txt') as file:
    f = file.read().strip()

n_idx = []
for idx in range(len(f)):
    val = f[idx:idx + 4]

    if val == '2022':
        n_idx.append(idx)

m = 0
for idx, start in enumerate(n_idx):
    try:
        stop = n_idx[idx + 4]
        s = f[start:stop]

        m = max(m, len(s))
    except IndexError:
        pass

print(m)  # 2000