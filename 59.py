n = 97 + 321 - 8
s = 0

while n:
    s += n % 3
    n //= 3

print(s)  # 6