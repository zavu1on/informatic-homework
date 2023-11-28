# 3 -> 9 -> 12 -> 20


def func(start, end):
    arr = [0] * 1000
    arr[start] = 1

    for i in range(start, end):
        arr[i + 1] += arr[i]
        arr[i + 3] += arr[i]
        arr[i * 2] += arr[i]

    return arr[end]


print(
    func(3, 9) *
    func(9, 12) *
    func(12, 20)
)  # 234
