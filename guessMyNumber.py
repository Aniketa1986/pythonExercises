# Python Programming for the Absolute Beginner
# Chapter 3
# Challenge 3
# Modify the Guess My Number game so that the player has a
# limited number of guesses. If the player fails to guess in time,
# the program should display an appropriately chastising message.

import random

print("\tWelcome to 'Guess My Number'! It is the best game ever, I swear!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 5 attempts.\n")

# set the initial values
theNumber = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 0
maxTries = 5

# guessing loop
while tries != maxTries:
    tries += 1
    if guess > theNumber:
        print("Lower...")
        guess = int(input("Take a guess: "))
    elif guess < theNumber:
        print("Higher...")
        guess = int(input("Take a guess: "))
    else:
        print("You guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!\n")
        break

print("\n\nWhat a shame! You had", maxTries, "attempts and still you sucked! LOOOOOSEEEEER!\n")
print("BTW Loser, number was", theNumber)
input("\n\nPress the enter key to exit.")
