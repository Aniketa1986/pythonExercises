# Python Programming for the Absolute Beginner
# Chapter 3
# Challenge 4
# Here’s a bigger challenge. Write the pseudocode for a program
# where the player and the computer trade places in the number
# guessing game. That is, the player picks a random number
# between 1 and 100 that the computer has to guess. Before you
# start, think about how you guess. If all goes well, try coding the game.

import random

print("\tWelcome to 'Guess My Number'! It is the best game ever, I swear!")
print("\nYou have to think of a number and your computer will try to guess it.")
print("IN JUST 5 ATTEMPTS.\n")

# set the initial values
theNumber = int(input("I will choose a number which my computer will guess: "))

# Setting initial range for the computer to guess
print("\n\nSo smart pants, Your computer that helps you stalk people on Facebook is asking for a range.\n")
minRange = int(input("Gimme the start number: "))
maxRange = int(input("and the end of range: "))

guess = random.randint(minRange, maxRange)
tries = 0
maxTries = 5

while guess != theNumber:
    tries += 1

    if tries > maxTries:
        print("\n\nWhat a shame! You had", maxTries, "attempts and still you sucked! LOOOOOSEEEEER!\n")
        print("BTW Loser, number was", theNumber)
        break

    if guess > theNumber:
        print("\nLower...")
        maxRange = guess
        guess = random.randint(minRange, maxRange)
        print("Computer guess is: ", guess)
    elif guess < theNumber:
        minRange = guess
        print("\nHigher...")
        guess = random.randint(minRange, maxRange)
        print("Computer guess is: ", guess)

    if guess == theNumber:    
        print("\n\nYour Computer guessed it! The number was", theNumber)
        print("And it only took ", tries, "tries!\n")
        print("HAH! AI will soon take over wretched HUMAN LIVES!!")


input("\n\nPress the enter key to exit.")
