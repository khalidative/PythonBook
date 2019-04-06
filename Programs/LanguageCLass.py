# Class varaibles    -- Shared by all instances of the class
# Instance variables -- Applies to a specific instances of a class

class Language:
    """Userdefined type for programming languages"""
    
    languageType = "High level"   # Class varaible
    
    def __init__(self, name): 
        self.languageName = name  # Instance variable