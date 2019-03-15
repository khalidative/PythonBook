#====================================================================
# Python program for the orbital distance problem
#====================================================================
from math import sqrt, cos, sin, pi

# The orbiting point is (x,y)
# A fixed point is always (100, 0),
# (p_x, p_y). Change them as necessary.
p_x = 100
p_y = 0

# number of radians in 10 degrees
radians = 10 * pi/180

# The cosine and sine of 10 degrees
cos10 = cos(radians)
sin10 = sin(radians)

# ask the satllites starting point from the user
x1, y1 = eval(input("Enter the satellites initial coordinates (x1,y1):"))

# calculate the initial distance d1
d1 = sqrt((p_x - x1)**2 + (p_y - y1)**2)

# calculate the new location (x2, y2) of the satellite after movement 
x2 = x1*cos10 - y1*sin10 

y2 = x1*sin10 + y1*cos10

# Compute the new distance d2
d2 = sqrt((p_x - x2)**2 + (p_y - y2)**2)

# Print the difference in the distances
print("Difference in the distances: %.5f" % (d2 - d1))










































