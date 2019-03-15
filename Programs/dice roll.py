from random import randrange

# skiping the seed setup

sides = 6

while 1:
    diceCount = int(input("Enter the number of dice to throw :"))
    if diceCount == 0:
        break
    for i in range(1, diceCount + 1):
        dieValue = randrange(1,sides + 1)
        print("%i " % (dieValue), end = " " )







































