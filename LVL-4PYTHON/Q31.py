def count_zeroes():
    count = 0

    for num in range(1, 1001):
        temp = num

        while temp > 0:
            if temp % 10 == 0:
                count = count + 1

            temp = temp // 10

    return count


print(count_zeroes())