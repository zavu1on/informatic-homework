print('a c b F')

for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (a and (not c)) or ((not a) and b and c)

            print(a, c, b, int(f))
