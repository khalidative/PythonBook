#========================================================
# Python program to calculates the factorial of a number
#========================================================

def factorial(x):
    """This is a recursive function
    that calculates the factorial of 
    an integer"""

    if x == 1: # recursive calls terminates when this condition is met
        return 1
    else:
        return (x * factorial(x-1)) # The function calls itself

while 1:
    num = eval(input("Enter an number: "))
    if num == -1:
        break
    print("The factorial of", num, "is", factorial(num))
    














    















