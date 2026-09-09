def is_prime(num):
    if num < 2:
        return False

    i = 2

    while i * i <= num:
        if num % i == 0:
            return False
        i = i + 1

    return True


def digit_sum(num):
    total = 0

    while num > 0:
        total = total + (num % 10)
        num = num // 10

    return total


def count_numbers():
    count = 0

    for num in range(2, 1000000):
        if is_prime(num) and digit_sum(num) == 14:
            count = count + 1

    return count


print(count_numbers())