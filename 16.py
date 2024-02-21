from ipaddress import ip_network

count = 0
for i in ip_network('99.64.0.0/255.192.0.0'):
    arr = [bin(int(i))[2:] for i in str(i).split('.')]
    arr = str(int(''.join(arr)))

    if arr.endswith('11'):
        count += 1

print(2 ** 20)
print(count)