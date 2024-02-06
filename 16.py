def f(x):
    y = str(x % 4)
    y += str(x % 2)
    y += str(x % 3)

    return int(y)


for i in range(10, 100):
    if f(i) == 311:
        print(i)  # 19
        break
