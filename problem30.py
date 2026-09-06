# Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is equal to 10, and one of the digits is more than 7 then print "Success", otherwise print "Failure".
num = int(input())

hundred = (num // 100) % 10
tens = (num // 10) % 10

if hundred + tens == 10 and (hundred > 7 or tens > 7):
    print("Success")
else:
    print("Failure")