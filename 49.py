print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x and ((not y) and z and (not w) or y and (not z))

                if f == 1:
                    print(x, y, z, w)