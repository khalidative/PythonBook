def foo():  # foo's defninition
    #------------------------------------foo's local scope starts
    a = 0                # foo's local variable
    print(a)
    #------------------------------------foo's local scope ends

#------------------------------------------------Global scope
    
print(a) #--------------------------> a is not defined in this scope!

#------------------------------------------------Global scope