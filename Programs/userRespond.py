#====================================================================
# This program prints the time it took the user to repsond in seconds
#====================================================================
from time import clock # import the clock method 

print("User respond! : ")
startTime = clock()
input()
endTime = clock()
print("It took you %f seconds to respond " % (endTime - startTime))









































