# УАПАП
print(int('40101', 5) + 1)  # 2527

from itertools import product
arr = list(product('АПРСУ', repeat=5))
arr = list(map(lambda el: ''.join(el), arr))

print(arr.index('УАПАП') + 1, sep='\n')  # 2527