#==================================================================
# Python program that demonstrates the use of super() in python
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
        super().__init__()     # Call the constructor of the parent
        print("It's name is Jupiter")

    def whoAmI(self):
        """This method overrides the
        whoisThis() method of the base class"""
        #print("I am Jupiter")-----------------------------------------!
        super().whoAmI()       # calling the super function 
                               # of the base class

    def brag(self):
        print("I have 79 moons!!")
#------------------------class Jupiter-----------------------------

#----------------Instantiation and method calls--------------------
celestial_body = CelestialBody() # Instatiating the object
jupiter = Jupiter()              # Instatiating the object

celestial_body.whoAmI()          # calls the base class method
jupiter.whoAmI()                 # calls the derived class method
#----------------Instantiation and method calls--------------------




































































































