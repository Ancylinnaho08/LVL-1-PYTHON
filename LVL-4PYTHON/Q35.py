def find_lcm(a, b):
    if a > b:
        lcm = a
    else:
        lcm = b

    while True:
        if lcm % a == 0 and lcm % b == 0:
            return lcm

        lcm = lcm + 1


a, b = map(int, input().split())

print(find_lcm(a, b))