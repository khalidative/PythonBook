#=====================================================================
# Three second count down timer!
#=====================================================================
from time import sleep    # Import the sleep method

timer = int(3)            # Initialize the timer to a predefined value

print("Count down starts... %i" %timer)

while timer > 0:
    sleep(1)
    timer -= 1
    print(timer)
    
sleep(1)