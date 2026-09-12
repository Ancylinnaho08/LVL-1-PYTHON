# Write a loop program to print the two-digit odd numbers whose sum of digits is 7.
for i in range(10, 100):
    if i % 2 != 0:
        tens = i // 10
        ones = i % 10

        if tens + ones == 7:
            print(i)