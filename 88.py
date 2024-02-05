for x in range(17):
    a = int(f'66{x}63', 17)
    b = int(f'5{x}810', 17)
    s = a - b

    if s % 11 == 0:
        print(s // 11)  # 8389
        break