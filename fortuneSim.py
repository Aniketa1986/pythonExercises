# chapter 3, exercise 1
# Fortune Cookie
# Write a program that simulates a fortune cookie. The program should display one of five unique fortunes, at random, each time it’s run.

import random

#generate random number between 1 and 5
randomNum = random.randint(1,5)

#Unique fortune messages
fortune1 = "Some days you are pigeon, some days you are statue. Today, bring umbrella."
fortune2 = "Wise husband is one who thinks twice before saying nothing."
fortune3 = "Dijon vu -- the same mustard as before."
fortune4 = "The fortune you seek is in another cookie."
fortune5 = "A day without sunshine is like night."

print("Welcome to the fortune cookie simulator.\nHere you will get motivated like never. \n")

if randomNum == 1:
    print(fortune1)
elif randomNum == 2:
    print(fortune2)
elif randomNum == 3:
    print(fortune3)
elif randomNum == 4:
    print(fortune4)
else: print(fortune5)

print("Now get back to your work!")
