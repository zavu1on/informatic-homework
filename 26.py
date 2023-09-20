from itertools import product

arr = list(map(lambda el: ''.join(el), product(sorted('КРАТЕР'), repeat=6)))

s1 = arr.index('КАРЕТА')
s2 = arr.index('РАКЕТА')

print(s2 - s1 - 1)  # 7559