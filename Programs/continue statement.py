#===============================================================
# Print all charecters of a given string except i's
#===============================================================

userString = input("Enter a string : ")

for val in userString:
    if val == "i":
        print("An \"i\" was skipped here.")
        continue
    print(val)
else:
    print("...Done")





























