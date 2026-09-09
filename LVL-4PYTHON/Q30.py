def is_prime(num):
    if num < 2:
        return False

    i = 2

    while i * i <= num:
        if num % i == 0:
            return False
        i = i + 1

    return True


for num in range(99999999, 9999999, -1):
    if is_prime(num):
        print(num)
        break