def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def count_primes():
    count = 0

    for num in range(100, 1000):
        if is_prime(num):
            count = count + 1

    return count


print(count_primes())