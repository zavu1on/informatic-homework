print('x y z')

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (y <= (z and x)) or (x == y)

            if f == 0:
                print(x, y, z)

