#===================================================================
# Demonstrating the nested if statements.
# Print the appropriate message for the different values of num
#===================================================================

num = int(input("Enter a number: "))   # Input from the user
                                       # convert it to the type int

if num >= 0:
    if num == 0:
        print("You entered zero!")
    else:
        print("You entered a positive number!")
else:
    print("You enterd a negative number!")