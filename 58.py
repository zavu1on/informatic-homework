print('x y z')

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (y <= x) and z and (not (z == y))

            if f == 1:
                print(x, y, z)

