def sum_odd_numbers():
    total = 0

    for num in range(1, 10):
        if num % 2 != 0:
            total = total + num

    return total


print(sum_odd_numbers())