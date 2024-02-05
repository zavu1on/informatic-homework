for i in range(1, 26):
    j = i
    n = ''
    while i != 0:
        n += str(i % 6)
        i //= 6
    if n[-1] == '4':
        print(j)

"""
4
24
25
"""