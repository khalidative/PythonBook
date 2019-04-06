# Not a good practice to import all names
from math import *  # import all names in the math module
# Warning 1 - Unable to detect undefined names

print("the square root of 12000 is ", sqrt(12000))
# Warning 2 - sqrt may be undefined or defined from start imports.