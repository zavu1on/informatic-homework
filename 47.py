print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x and (not w) and (y or not z)

                if f == 1:
                    print(x, y, z, w)