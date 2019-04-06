class Point:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        """This function returns the point object
        in a tuple format as string
        Example: "(7, 12, 0)" """
        #print("x = ", self.x, ", y = ", self.y, ", z = ", self.z)
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)
    
    def __add__(self,other):
        """ This method defines how the +
        operator is applied on two Point objects
        p1 + p2 => p1.__add__(p2) => Point.__add__(p1, p2)"""
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __ge__(self,other):
        """ This method defines how the +
        operator is applied on two Point objects
        p1 >= p2 => p1.__ge__(p2) => Point.__ge__(p1, p2)"""
        # Calculate the magnitude of self
        self_magnitude = (self.x ** 2) + (self.y ** 2) + (self.z ** 2)
        # Calculate the magnitude of other
        other_magnitude = (other.x ** 2) + (other.y ** 2) + (other.z ** 2)
        return self_magnitude >= other_magnitude