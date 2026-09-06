# Get a three-digit number from user. If the sum of the one's digit and hundred's digit is less than 10, then print "Success", otherwise print "Failure".
num = int(input())

hundred = num // 100
ones = num % 10

if hundred + ones < 10:
    print("Success")
else:
    print("Failure")