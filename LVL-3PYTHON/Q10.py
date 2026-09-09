#Get a number from user, find the number of digits, and print it.
def count_digits(num):
    count = 0

    while num > 0:
        num = num // 10
        count = count + 1

    return count


num = int(input())
print(count_digits(num))