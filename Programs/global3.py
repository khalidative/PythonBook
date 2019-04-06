x = 20 # x is a global variable

def printx():
    global x   # Now the global variable x can be modified
    x = x + 4  # No error raised 
    print("This is the value of x inside printx: %i" %x) 

printx()
print("This is the value of x outside printx: %i" %x)