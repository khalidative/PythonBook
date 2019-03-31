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







































