with open('data/k7-m7.txt') as file:
    f = file.read().strip()

s = f.replace('A', ' ').replace('B', ' ').split()
a1 = len(s)

c = ''.join(s)
s = f.replace('C', '')
s = c + s

print(a1, f[:35], s[:35])  # 14 AAACBBBCBBBBCCAAAAAABBBBBBBBCCAAAAA CCCCCCCCCCCCCCCCCCCCCCCCAAABBBBBBBA