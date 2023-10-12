with open('data/24-232.txt') as file:
    f = file.read().strip()

zero_idx = []
for idx, val in enumerate(f):
    if val == '0':
        zero_idx.append(idx)

m = ''
for idx, start in enumerate(zero_idx):
    try:
        stop = zero_idx[idx + 1]
        s = f[start + 1:stop]

        if sum(map(int, s)) % 5 == 0:
            m = max(m, s, key=len)
    except IndexError:
        pass

print(sum(map(int, m)))  # 375