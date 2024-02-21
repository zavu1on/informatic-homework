from ipaddress import ip_network
from collections import Counter

count = 0
for i in ip_network('117.32.0.0/255.224.0.0'):
    i = str(i)
    c = Counter(i.split('.'))
    v = sorted(c.values())

    if v == [1, 1, 2]:
        count += 1

print(count)  # 40640