# Author MB 12/03/2021

total = 0
while True:
    num = input("What is the number: ")
    if num == "-1":
        break
    else:
        total += int(num)

print("the sum of all the numbers are {0}".format(total))
