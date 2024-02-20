print('x y z')

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x or y) <= (x == z)

            if f == 0:
                print(x, y, z)

