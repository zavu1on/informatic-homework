from ipaddress import ip_network

count = 0
for i in ip_network('213.0.0.0/255.192.0.0'):
    arr = [bin(int(i))[2:] for i in str(i).split('.')]
    arr = str(int(''.join(arr)))

    if '111' in arr:
        count += 1

print(count)
