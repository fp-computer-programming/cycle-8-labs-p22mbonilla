# Author MB 12/01/2021

def sum_to(num):
    total = 0
    for val in range(int(num)+1):
        total += val
    return total

number = input("give me a number: ")
print(sum_to(number))
