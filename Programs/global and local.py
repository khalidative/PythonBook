#-------------------------------------------------------Global scope
a = 10           # Global variable
def foo():       # foo's definition, part of the global scope
#-------------------------------------------------------Global scope
    #------------------------------------foo's local scope starts
    a = 0        # foo's local variable
    return a     # The local variable a is accessed (a = 0)
    #------------------------------------foo's local scope ends

#-------------------------------------------------------Global scope
print("The value of 'a' in foo is ",foo())
print("The value of 'a' in global scope is ", a)
#-------------------------------------------------------Global scope