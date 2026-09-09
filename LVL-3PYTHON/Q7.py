#Get two numbers from user and compare them. If they are the same, print Same; otherwise print Not Same.
def compare_numbers(a, b):
    if a == b:
        print("Same")
    else:
        print("Not Same")


a, b = map(int, input().split())
compare_numbers(a, b)