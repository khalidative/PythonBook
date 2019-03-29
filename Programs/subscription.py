#======================================================================
# Python program that demonstrates encapsulation in python
#======================================================================

#------------------------class Subscription----------------------------
class Subscription:
    
    #Variable 
    
    def __init__(self):
        "The constructor of the class"
        print("You created a new subscription")
        self.__billingPeriod = 1 # Default period in months

    def GetBillingPeriod(self):
        print("Current billing period: {}".format(self.__billingPeriod))

    def SetBillingPeriod(self):
        billingPeriod = eval(input("Enter the new billing period: "))
        self._Subcscription__billingPeriod = billingPeriod
        print("The new billing period: ", self.__billingPeriod)
#------------------------class Subscription----------------------------

#-------------------Instantiation and method calls---------------------
sub1 = Subscription()

#print("The current billing period: ",sub1.__billingPeriod)
                          # can't directly access the private variable
                          # So interpreter raises error when executed

sub1.GetBillingPeriod()   # Accessing the private varaible with the
                          # with the logic provided by the getter
                          # method

sub1.__billingPeriod = 12 # Can't directly access the private variable  

print("An attempt was made to change the private varaible to 12")
sub1.GetBillingPeriod()

sub1.SetBillingPeriod()   # Accessing the private varaible with the
                          # with the logic provided by the setter
                          # method
sub1.GetBillingPeriod()
#-------------------Instantiation and method calls---------------------



            
















