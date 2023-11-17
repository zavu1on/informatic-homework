from itertools import product

for i in range(6):
    for x in product('123456789', repeat=i):
        for y in '123456789':
            s = f'32{"".join(x)}54{y}123'
            n = int(s)

            if n % 519 != 0:
                continue
            if len(s) % 2 != 0:
                continue
            if sum(map(int, s[:len(s) // 2])) != sum(map(int, s[len(s) // 2:])):
                continue

            print(n, n // 519)
"""
321525543123 619509717
322167546123 620746717
323724546123 623746717
324366549123 624983717
325281546123 626746717
325923549123 627983717
"""