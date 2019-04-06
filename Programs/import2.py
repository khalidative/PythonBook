import math as m

num = eval(input("Enter a number: "))

num_root = m.sqrt(num)   # Observe that the module handle is 'm'
num_root = math.sqrt(num)# math is not recognised

print("The square root of ", num, " is ", num_root)