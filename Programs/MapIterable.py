#------------------------class MapIterable--------------------------
class MapIterable:
    def __init__(self, iterable):
        self.items = []
        self.__mapper(iterable)

    def mapper(self, iterable):
        for item in iterable:
            self.items.append(item)

    __mapper = mapper # Private copy of original the mapper() method
    
#------------------------class MapIterable--------------------------

#--------------------class MapIterableDerived-----------------------
class MapIterableDerived(MapIterable):

    def mapper(self, keys, values):
        # Gives a new signature for the mapper() method
        # but does not break the __init__() method of the base class
        for item in zip(keys, values): 
            self.items.append(item)
            
#--------------------class MapIterableDerived-----------------------