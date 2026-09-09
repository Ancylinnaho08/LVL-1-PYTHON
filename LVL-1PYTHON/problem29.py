# Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is greater than 10, then print "Success", otherwise print "Failure".
num = int(input())

hundred = (num // 100) % 10
tens = (num // 10) % 10

if tens + hundred > 10:
    print("Success")
else:
    print("Failure")