from itertools import product

alph = 'ЧОАНИМЕ'
arr4 = product(alph, repeat=4)
arr5 = product(alph, repeat=5)
arr6 = product(alph, repeat=6)
c = 0

for i in [*arr4, *arr5, *arr6]:
    if i.count('М') == 3:
        c += 1

print(c)  # 4704