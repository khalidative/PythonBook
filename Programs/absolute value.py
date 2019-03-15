#==============================================================
# Evaluate absolute value of a number
#==============================================================
def absolute_value(num):
	"""This function returns the absolute
	value of the number passed as an argument"""

	if num >= 0:
		return num
	else:
		return (-num)


userInput = eval(input("Enter a number: ")) # evaluate users input

print("It's absolute value is " + str(absolute_value(userInput)))




















    















