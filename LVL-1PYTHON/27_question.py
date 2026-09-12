# Get a three-digit number from user. If the sum of the digits is 10 then print "Success", otherwise print "Failure".
num = int(input())

hundred = num // 100
tens = (num // 10) % 10
ones = num % 10

if hundred + tens + ones == 10:
    print("Success")
else:
    print("Failure")