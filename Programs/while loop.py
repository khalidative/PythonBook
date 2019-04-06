# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:41:08 2019

@author: Mohamed Khalid
"""

#===============================================================
# Examples of loops that terminate and infinite loops
#===============================================================

# Assignments
var1 = 1
var2 = 2
var3 = 3

#---------------------------------------- Loop is never executed
while (0 + 1 - var1):
    print(var1)
    var1 += 1

#---------------------------------------------- Terminating loop

while (var1 <= 10):
    print(var1)
    var1 += 1

#---------------------------------------------- Terminating loop
while (var2 >= -10):
    print(var2)
    var1 -= 5

#------------------------------------------------- Infinite loop
while (var3 != 10):
    print(var3)
    var3 += 6

#------------------------------------------------- Infinite loop
while (1):
    print(var1)