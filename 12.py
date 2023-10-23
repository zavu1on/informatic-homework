c = 0
m = 3439

for i in range(3439, 7411):
    if i % 2 != i % 6:
        if any([i % 9 == 0, i % 10 == 0, i % 11 == 0]):
            c += 1
            m = max(m, i)

print(c, m)  # 683 7407
