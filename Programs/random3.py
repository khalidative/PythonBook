from random import randrange, seed

seed(10) # The seed is 10

for i in range(3):
    print(i + 1, ")", randrange(1, 10))
print("----------")

seed(14) # Change the seed to something else

for i in range(3):
    print(i + 1, ")", randrange(1, 10))
print("----------")

seed(3)

for i in range(3):
    print(i + 1, ")", randrange(1, 10))
print("----------")