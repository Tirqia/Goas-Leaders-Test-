def triangular(n):
    if n < 0:
        return 0
    return (n * (n + 1)) // 2


print(triangular(4))

# 2


def triangular(n):
    if n < 0:
        return 0
    result = 0
    for i in range(1, n + 1):
        result += 1
    return result


print(triangular(4))
