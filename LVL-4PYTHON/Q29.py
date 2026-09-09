def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


for num in range(9999, 999, -1):
    if is_prime(num):
        print(num)
        break