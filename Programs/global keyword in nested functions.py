a = 10
print("a in the global scope before calling foo: ", a)

def foo():
    a = 40
    print("a in local scope before calling nested_foo: ", a)
    
    def nested_foo():
        global a
        a = 20
    
    nested_foo()
    print("a in local scope after calling nested_foo: ", a)

foo()
print("a in the global scope before calling foo: ", a)

    

    













        