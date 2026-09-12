#  Write a loop program to print the two-digit even numbers whose sum of digits is 6.
for i in range(10, 100):
    if i % 2 == 0:
        tens = i // 10
        ones = i % 10

        if tens + ones == 6:
            print(i)