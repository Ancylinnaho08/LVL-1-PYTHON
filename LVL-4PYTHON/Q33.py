def is_non_decreasing(num):
    digits = str(num)

    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False

    return True


def count_numbers():
    count = 0

    for num in range(1000, 10000):
        if is_non_decreasing(num):
            count = count + 1

    return count


print(count_numbers())