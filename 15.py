from itertools import product

for i in range(5):
    arr = product('0123456789', repeat=i)
    for a in arr:
        for b in '0123456789':
            s = int(f'4{"".join(a)}1{b}009')

            if s ** 0.5 % 1 == 0:
                print(int(s ** 0.5), s)
"""
2003 4012009
6497 42211009
63997 4095616009
64997 4224610009
69003 4761414009
"""