resp = 0

for i in range(100000, 888888 + 1):
    c = 0
    sum_ = 0

    for x in str(i):
        n = int(x)
        sum_ += n
        if n % 2 != 0:
            c += 1

    if c > 2:
        continue

    if sum_ % 6 == 0 and sum_ % 4 != 0:
        resp += 1

print(resp)  # 32838

