with open('data/24-268.txt') as file:
    f = file.read().strip()


alph = '0123456789ABCDEFGHI'
temp = ''
max_val = 0
max_str = ''

for i in f:
    if not temp and i in alph:
        temp += i
    elif temp:
        if i in alph:
            temp += i
        else:
            n = int(temp, 19)

            if n % 2 == 0:
                if n > max_val:
                    max_val = n
                    max_str = temp

            temp = ''

print(max_str)  # GGA55CF9