#==================================================================
# Python program that illustrates how inheritance works in python
#==================================================================

#------------------------class CelestialBody-----------------------
class CelestialBody:
    """All the data attributes and method attributes
    of this class are inherited by the class "DerivedClass" """
    
    def __init__(self):
        "The constructor of the class"
        print("A celestial body was created")

    def whoAmI(self):
        print("I am a celestial body")

    def speak(self):
        print("I'm outside the earth's atmospere")
#------------------------class CelestialBody-----------------------

#------------------------class Jupiter-----------------------------
class Jupiter(CelestialBody):
    """This class inherits the 
    attributes of the class "BaseClass"
    defined above"""
    
    def __init__(self):
        "The constructor of the class"
        super().__init__() # Call the constructor of the parent
        print("It's name is Jupiter")

    def whoAmI(self):
        """This method overrides the
        whoisThis() method of the parent class"""
        print("I am Jupiter")

    def brag(self):
        print("I have 79 moons!!")
#------------------------class Jupiter-----------------------------

#----------------Instantiation and method calls--------------------
jupyter = Jupiter()   # Calls Jupiter's constructor and creates an
                      # creates a Jupiter instance object
jupyter.whoAmI()      # This method is defined in class Jupiter
jupyter.speak()       # This method is defined in class CestialBody
jupyter.brag()        # This method is defined in class Jupter
#----------------Instantiation and method calls--------------------


















































