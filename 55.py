n = 5 * 36 ** 7 + 6 ** 10 - 36
count = 0

while n:
    if n % 6 == 5:
        count += 1
    n //= 6

print(count)  # 9