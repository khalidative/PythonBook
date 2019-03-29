#==================================================================
# Python program that illustrates polymorphism in python
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
        whoisThis() method of the base class"""
        print("I am Jupiter")

    def brag(self):
        print("I have 79 moons!!")
#------------------------class Jupiter-----------------------------

#------------------------class Saturn------------------------------
class Saturn(CelestialBody):
    """This class inherits the 
    attributes of the class "BaseClass"
    defined above"""
    
    def __init__(self):
        "The constructor of the class"
        super().__init__() # Call the constructor of the parent
        print("It's name is Saturn")

    def whoAmI(self):
        """This method overrides the
        whoisThis() method of the base class"""
        print("I am Saturn")

    def brag(self):
        print("My rings are made up of ice")
#------------------------class Saturn------------------------------

#---------------------function definition--------------------------
def callBrag(Celestial_Body): 
    """This function is a common interface, 
    it calls brag method of the Celestial body
    passed as an argument"""
    Celestial_Body.brag() 

#---------------------function definition--------------------------

#---------------Instantiation and function calls-------------------
# Instatiating the objects
jupiter = Jupiter()
saturn = Saturn()

# Pass the objects as arguments to the common interface
# observe that the appropriate method instance ins called 
# based on the argument passed
callBrag(jupiter)
callBrag(saturn)

#---------------Instantiation and function calls-------------------



















































