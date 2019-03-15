#====================================================================
# Time taken to add the forst million natural numbers
#====================================================================
from time import clock # import the clock method 

sum = 0 # initialize sum as 0

print("started adding")
startTime = clock()

for i in range(10000000):
    sum += i

endTime = clock()
print("It took %f seconds " % (endTime - startTime))









































