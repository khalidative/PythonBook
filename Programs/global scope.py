#---------------------------------------------------Global scope
x = 10      # Global variable
y = 20      # Global variable
z = 30      # Global variable
def foo(): # foo's definition, part of the global scope
#---------------------------------------------------Global scope
    #------------------foo's local scope starts
    a = 0 # foo's local variable
    print(a, x, y, z, b) # foo can acces global varaibles 
    #------------------foo's local scope ends

#---------------------------------------------------Global scope
b = 40      # Global variable
foo()       # making a call to function foo

#---------------------------------------------------Global scope