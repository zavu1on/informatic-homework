def f(a, b):
    s = ''
    while a != 0:
        s += str(a % b)
        a //= b
    return s == s[::-1]


for i in range(20, 2023 ** 3, 10):
    s = str(i)
    if '2' not in s or s[-1] != '0':
        continue
    if s.find('2') > s.rfind('0'):
        continue

    if f(i, 3) and f(i, 7):
        print(i, sum(map(int, oct(i)[2:])))

"""
8200 3
233920 15
532900 18
3316520 25
24919360 25
184827640 25
...
"""