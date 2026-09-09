# Write a loop program to print the sum of two-digit odd numbers whose ten's digit is 7.
sum = 0

for i in range(10, 100):
    if i // 10 == 7 and i % 2 != 0:
        sum = sum + i

print(sum)