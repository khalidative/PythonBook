def printLocalx():
    x = 10    # Local variable, scope lines 2 - 3 
    print("This is printLocalx() function's value of x :",x)
    print("This is printLocalx() function's value of y :",y)    
    # local variable x gets deleted
    
x = 20      # Global variable, scope lines 1 - 8
y = 40      # Global variable, scope lines 1 - 8
printLocalx()
print("Value outside the function:",x)



















    















