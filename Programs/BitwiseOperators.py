#======================================
# Assignments
#======================================

#-----In Decimal------In Binary--------
#--------------------------------------
x =      60         # 0011 1100
y =      13         # 0000 1101
z =       0         # 0000 0000

#======================================
# Using bitwise operators
#======================================

z = x & y      # 12 = 0000 1100
print("Line 1 - value of z is ", z)

z = x | y      # 61 = 0011 1101
print("Line 2 - value of z is ", z)

z = x ^ y      # 49 = 0011 0001
print("Line 3 - value of z is ", z)

z = ~x         #-61 = 1100 0011
print("Line 4 - value of z is ", z)

z = x << 2     #240 = 1111 0000
print("Line 5 - value of z is ", z)

z = x >> 2     # 15 = 0000 1111
print("Line 6 - value of z is ", z)