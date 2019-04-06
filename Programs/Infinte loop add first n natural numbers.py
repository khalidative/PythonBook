#===========================================================
# This program adds the first "n" natural numbers
#===========================================================

n = int(input("Enter the value of n: "))

# Initialize sum and counter variables
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1     # Update to the counter variable is skipped
    
print("The sum is: ", sum)
