# game.py 

import random

import os

from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

user_name = os.getenv("USER_NAME")

user_name=user_name.upper()

print(user_name) # reads the variable from the environment


print("ROCK, PAPER, SCISSORS, SHOOT!")

# Ask for a user input

x=input("PLEASE CHOOSE ONE OF EITHER 'ROCK','PAPER' OR 'SCISSORS': ")

x=x.upper()

#Validate the user input

if  x == "ROCK" or (x == "PAPER") or (x == "SCISSORS"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()

print ("USER CHOSE: ", x) 

#generate a computer choice

valid_options = ["ROCK","PAPER","SCISSORS"] #list to contain different variables

c = (random.choice(valid_options))

print("COMPUTER CHOSE:", c)

# Determine the  winner

if (c == x):
    print("TIE")
elif(c == "ROCK") and (x == "SCISSORS"):
    print("YOU LOST")
elif(c == "SCISSORS") and (x == "ROCK"):
    print("YOU WON")
elif(c == "PAPER") and (x == "ROCK"):
    print("YOU LOST")
elif(c == "ROCK") and (x == "PAPER"):
    print("YOU WON")
elif(c == "SCISSORS") and (x == "PAPER"):
    print("YOU LOST")
elif(c == "PAPER") and (x == "SCISSORS"):
    print("YOU WON") 


