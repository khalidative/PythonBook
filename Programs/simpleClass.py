#========================================================
# Defining a simple class
#========================================================

class SimpleClass:
    """An Example of a simple class"""
    
    # Variable assignments
    a = 3.1415
    b = "Ipython"
    c = -12 * 3
    
    # Method definitions
    def __init__(self): # Automatically invoked at class instantiation
        self.a = 10

    def sayHello(self): 
        return "Hello user!!"

    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z