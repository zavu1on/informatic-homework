def f(r):
    b = bin(r)[2:]

    if b.endswith('01') and b[:-2].count('1') % 2 == 0:
        return True

    if b.endswith('10') and b[:-2].count('1') % 2 != 0:
        return True

    return False


count = 0
for r in range(16, 33):
    if not f(r):
        count += 1

print(count)  # 13