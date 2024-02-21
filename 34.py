from ipaddress import ip_network

count = 0
for i in ip_network('192.168.32.160/255.255.255.240'):
    arr = [bin(int(i))[2:] for i in str(i).split('.')]
    arr = str(int(''.join(arr)))
    print(arr)
    if arr.count('0') > 21:
        count += 1

print(count)