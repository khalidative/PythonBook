def foo():       
    #------------------------------------foo's local scope starts
    a = 20           # foo's local variable
    print("a in foo: ", a)
    #------------------------------------foo's local scope ends
    def nested_foo():
        nonlocal a   # Now 'a' is a non local variable 
        a = a + 20 
        print("a in nested_foo: ", a)
    nested_foo()
    print("a in foo: ", a)
#------------------------------------------------Global scope
foo()
#------------------------------------------------Global scope



    

    













