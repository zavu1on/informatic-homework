print('a b c F')

for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (a or not c) and (b or c)

            print(a, b, c, int(f))
