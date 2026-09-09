def count_odd_numbers():
    count = 0

    for num in range(1, 10):
        if num % 2 != 0:
            count = count + 1

    return count


print(count_odd_numbers())