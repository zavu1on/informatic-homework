from itertools import product
from collections import Counter

arr = product('КОМПЬЮТЕР', repeat=5)
c = 0

for i in arr:
    co = [i[1] for i in Counter(i).items()]

    if len(co) == 3 and co.count(2) == 2 and co.count(1) == 1:
        c += 1
    elif len(co) == 2 and co.count(4) == 1 and co.count(1) == 1:
        c += 1
    elif len(co) == 1 and co.count(5) == 1:
        c += 1

print(c)  # 7929
