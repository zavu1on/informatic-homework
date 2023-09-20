c = 0


def convert_to(number, base, upper=False):
    digits = '0123456789ab'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


for i in range(100000, 1000000):
    i_12 = convert_to(i, 12)[0]

    if i_12 == 'a':
        i_12 = '10'
    elif i_12 == 'b':
        i_12= '11'

    if i % int(i_12) == 0:
        c += 1

print(c)  # 477703
