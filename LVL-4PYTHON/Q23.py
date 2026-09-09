def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_sum():
    total = 0

    for num in range(2, 10):
        if is_prime(num):
            total = total + num

    return total


print(prime_sum())