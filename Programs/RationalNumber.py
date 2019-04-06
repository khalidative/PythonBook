#================================================================
# RationalNumber.py
#================================================================
class RationalNumber:
    """
    Objects of this class can represent a rational number
    """
    def __init__(self, n, d):
        self.__numerator = n       # Private variable
        if d != 0:
            self.__denominator = d # Private variable
        else:
            print("It's not a good idea to divide by zero")
    
    def GetNumerator(self):
        """ Returns the numerator of the fraction. """
        return self.__numerator

    def GetDenominator(self):
        """ Returns the denominator of the fraction. """
        return self.__denominator

    def SetNumerator(self, num):
        """ Sets the numerator of the fraction to n. """
        self.__numerator = num

    def SetDenominator(self, den):
        """
        Sets the denominator to den,unless d 
        is zero, in which case the method
        prints an error message
        """
        if den != 0:
            self.__denominator = den
        else:
            print("Error: zero denominator!")

    def __str__(self):
        """
        Make a string representation of a Rational object
        and return it to the caller
        """
        num = self.GetNumerator()
        den = self.GetDenominator()
        return str(num) + "/" + str(den)

# Client code that uses Rational objects
def main():
    x = RationalNumber(3, 6)
    y = RationalNumber(22, 60)
    
    print("x =", x)
    print("y =", y)
    
    x.SetNumerator(12)
    x.SetDenominator(23)
    y.SetNumerator(13)
    y.SetDenominator(29)
    
    print("x =", x)
    print("y =", y)

main()