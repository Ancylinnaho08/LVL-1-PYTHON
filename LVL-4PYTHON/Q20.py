def count_prime_numbers():
    count = 0

    for num in range(2, 10):
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            count = count + 1

    return count


print(count_prime_numbers())