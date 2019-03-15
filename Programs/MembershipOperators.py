#====================================================================
# Assignments
#====================================================================
x = 6
y = 7
li = [1, 2, 3, 4, 5 ];

#====================================================================
# Using membership operators
#====================================================================
if ( x in li ):
    print("Line 1 - x is available in the given list")
else:
    print("Line 1 - x is not available in the given list")

if ( y not in li ):
    print("Line 2 - y is not available in the given list")
else:
    print("Line 2 - y is available in the given list")

x = 4

if ( x in li ):
    print("Line 3 - x is available in the given list")
else:
    print("Line 3 - x is not available in the given list")







