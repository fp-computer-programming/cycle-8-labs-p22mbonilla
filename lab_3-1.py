# Author MB 12/02/2021

def sum_to(n):
    total = 0
    counter = 0
    while total <= n:
        total += counter
        counter += 1
    return total

num = int(input("what is my number: "))
res = sum_to(num)

print("the sum to " + str(num) + " is, " + str(res))
