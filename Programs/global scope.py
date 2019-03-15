#---------------------Global scope
x = 10      # Global variable
y = 20      # Global variable
z = 30      # Global variable
#---------------------Global scope
def foo(): # foo's defninition
    #------------------foo's local scope starts
    a = 0 # foo's local variable
    print(a, x, y, z, b) # foo can acces global varaibles 
    #------------------foo's local scope ends
#---------------------Global scope
b = 40      # Global variable
foo() # Calling foo
#---------------------Global scope





    















