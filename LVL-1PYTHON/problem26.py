# Get a two-digit number from user. If the sum of the digits is 10 then print "Success", otherwise print "Failure".
num = int(input())

tens = num // 10
ones = num % 10

if tens + ones == 10:
    print("Success")
else:
    print("Failure")