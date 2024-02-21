from ipaddress import ip_network

count = 0
for i in ip_network('250.135.101.80/255.255.255.248'):
    arr = [bin(int(i))[2:] for i in str(i).split('.')]
    arr = str(int(''.join(arr)))

    if arr.count('0') % 3 == 0:
        count += 1

print(count)