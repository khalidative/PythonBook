#===============================================================
# Print all characters of a string untill the first "i" is found
#===============================================================

userString = input("Enter a string : ")

for val in userString:
    if val == "i":
        print("Loop terminated")
        break
    print(val)
else:
    print("The letter i was not found in your string")