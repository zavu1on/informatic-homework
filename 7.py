def f(s):
    while '333' in s or '77777' in s:
        if '333' in s:
            s = s.replace('333', '77', 1)
        else:
            s = s.replace('77777', '7', 1)
    return s


s = '3' * 70
print(sum(map(int, f(s))))  # 17
