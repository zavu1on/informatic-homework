with open('data/24-258.txt') as file:
    f = file.read().strip()

# ATGTTT ACATAA
# TAA TGA TAG
# ATGTTTGTCAAACATAA

tmp = ''
for i in f:
    if not tmp and i == 'A':
        tmp += i
    elif tmp:
        tmp += i
        length = len(tmp)

        if not tmp.startswith('ATGTTT'[:length]) and length <= 6:
            if i == 'A':
                tmp = 'A'
            else:
                tmp = ''

        if tmp.endswith('ACATAA'):
            print(tmp)
            tmp = 'A'

        for j in ['TAA', 'TGA', 'TAG']:
            if j in tmp:
                if i == 'A':
                    tmp = 'A'
                else:
                    tmp = ''

tmp = ''
start_arr = []
end_arr = []
for idx in range(len(f)):
    s = f[idx:idx + 6]

    if s == 'ATGTTT':
        start_arr.append(idx)
    elif s == 'ACATAA':
        end_arr.append(idx)

for start, end in zip(start_arr, end_arr):
    s = f[start:end]

    if 'TAG' in s:
        continue
    if 'TGA' in s:
        continue
    print(s)
