# given number
given_number= 4
# since 1 is a factor
# of all number
# set the factorial to 1
factorial = 1
# iterate till the given number
for i in range(1, given_number + 1):
    factorial = factorial * i
    print("The factorial of ", given_number, " is ", factorial)
