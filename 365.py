with open('data/24-263.txt') as file:
    f = file.read().strip()

y_arr = [0]
for idx, val in enumerate(f):
    if val == 'Y':
        y_arr.append(idx)
y_arr.append(len(f) - 1)

m = 0
for idx, start in enumerate(y_arr[1:]):
    try:
        stop = y_arr[idx + 151]
        length = stop - start
        m = max(length, m)
    except IndexError:
        pass

print(m)  # 5149
