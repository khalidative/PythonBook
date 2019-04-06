#===============================================================
# Demonstrating the if..elif..else decision chain.
# Print the appropriate message for the different values of num
#===============================================================

num = 34

# Try these two variations yourself
# num = 0
# num = -205

if num >= 0:
    print("You've entered a positive number!")
elif num == 0:
    print("You've entered zero!")
else:
    print("You've entered a negative number!")