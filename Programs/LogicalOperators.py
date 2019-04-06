#====================================================================
# Assignments
#====================================================================
x = 5
y = 10

#====================================================================
# Using logical operators
#====================================================================
if( x and y ):
    print("Line 1 - x and y are true")
else:
    print("Line 1 - Either x is not true or y is not true")

if( x or y ):
    print("Line 2 - Either x is true or y is true or both are true")
else:
    print("Line 2 - Neither x is true nor y is true")

x = 0

if( x and y ):
    print("Line 3 - x and y are true")
else:
    print("Line 3 - Either x is not true or y is not true")

if( x or y ):
    print("Line 4 - Either x is true or y is true or both are true")
else:
    print("Line 4 - Neither x is true nor y is true")

if not( x and y ):
    print("Line 5 - Either x is not true or y is not true")
else:
    print("Line 5 - x and y are true")