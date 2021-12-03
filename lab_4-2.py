# Author MB 12/03/2021

def sum_to():
    for number in [2, 4, 6, 9, 10, 12, 13, 14]:
        if number % 2 == 0:
           continue
        print(number)
    print("Done")

sum_to()
