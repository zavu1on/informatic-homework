print('x y z')

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x or y) and (not z) and (not (z == x))

            if f == 1:
                print(x, y, z)

