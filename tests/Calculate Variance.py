# def variance(numbers):
#     mean = sum(numbers) / len(numbers)
#     variance = sum((y - mean) ** 2 for y in numbers) / len(numbers)

#     return variance


# print(variance([8, 9, 10, 11, 12]))


def variance(numbers):
    total = 0
    variance = 0
    for i in numbers:
        total += i
    total /= len(numbers)
    for i in numbers:
        variance += (i - total) ** 2
    return variance / len(numbers)


print(variance([8, 9, 10, 11, 12]))
