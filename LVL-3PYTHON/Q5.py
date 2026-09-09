#Get a number from user and count the number of zeros in that number.
def count_zeros(num):
    count = 0

    while num > 0:
        digit = num % 10

        if digit == 0:
            count = count + 1

        num = num // 10

    return count


num = int(input())
print(count_zeros(num))