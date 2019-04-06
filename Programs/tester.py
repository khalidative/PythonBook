#===============================================================
# Assignments
#===============================================================
x = 10
y = 10

#===============================================================
# Using identity operators
#===============================================================
if ( x is y ):
    print("Line 1 - x and y have same identity")
else:
    print("Line 1 - x and y do not have same identity")
if ( id(x) == id(y) ):
    print("Line 2 - x and y have same identity")
else:
    print("Line 2 - x and y do not have same identity")

x = 30

if ( x is y ):
    print("Line 3 - x and y have same identity")
else:
    print("Line 3 - x and y do not have same identity")
if ( x is not y ):
    print("Line 4 - x and y do not have same identity")
else:
    print("Line 4 - x and y have same identity")