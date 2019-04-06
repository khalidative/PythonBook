from random import randrange

# skiping the seed setup

sides = 7

while 1:
    diceCount = int(input("Enter the number of dice to throw :"))
    for i in range(diceCount):
        dieValue = randrange(1,sides)
        print("%i " % (dieValue), end = " " )