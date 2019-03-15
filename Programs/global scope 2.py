#------------------------------------------------Global scope
x = 10      # Global variable
#------------------------------------------------Global scope

def foo():  # foo's defninition
    #------------------------------------foo's local scope starts
    x = x + 40           # Trying to change the value of x ---------!
    a = 0                # foo's local variable
    print(a, x) # foo can acces global varaibles 
    #------------------------------------foo's local scope ends

#------------------------------------------------Global scope
foo()       # Calling foo
#------------------------------------------------Global scope





    















