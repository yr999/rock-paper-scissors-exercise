# game.py 

import random

print("Rock, Paper, Scissors, Shoot!")

# Ask for a user input

x=input("Please choose one of either 'rock', 'paper' or 'scissors'")


print("User Input")
print(x)

#Validate the user input

if  x == "rock" or (x == "paper") or (x == "scissors"):
    print("Valid")
else:
    print("oops invalid, please try again")
    exit()
print ("later messages") 




#generate a computer choice

valid_options = ["rock","paper","scissors"] #list to contain different variables

c = (random.choice(valid_options))

print("Computer Chose")

print(c)

# Determine the  winner