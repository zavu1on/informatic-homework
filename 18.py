from ipaddress import ip_network

count = 0
for i in ip_network('99.165.134.0/255.255.254.0'):
    arr = [bin(int(i))[2:] for i in str(i).split('.')]
    arr = str(int(''.join(arr)))

    if arr.count('1') % 3 == 0:
        count += 1

print(count)