# chapter 3
# Flip a coin 100 times and count heads and tails

import random

# declaring counter variables
headCount = 0
tailCount = 0
flipCounter = 0

# Generating a random number

while flipCounter < 100:
    flippedCoin = random.randint(0,1)
    flipCounter +=1
    if flippedCoin == 0:
        headCount += 1
    else: tailCount +=1

print("So you loser, the coin was flipped " + str(flipCounter) + " times.\nThe count of heads is " + str(headCount) + " and that of tails is " + str(tailCount) + ".")
