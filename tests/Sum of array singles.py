def repeats(arr):
    num_count = {}
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    sum_once = 0
    for num, count in num_count.items():
        if count == 1:
            sum_once += num

    return sum_once


arr = [16, 0, 11, 4, 8, 16, 0, 11]
print(repeats(arr))
