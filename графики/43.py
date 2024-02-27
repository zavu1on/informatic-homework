count = 0
for x in range(500):
    for y in range(500):
        f = not (((x > 6) and ((x + y) >= 5)) or (y >= 5))
        if f:
            count += 1

print(count)  # 35
