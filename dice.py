import random
import sys
prompt = "Do you want to throw the dice again? (Y/n)"

def dice_roller():
    while True:
        dice = random.randint(1,6)
        print("The dice is thrown.. and it lands on: " + str(dice))
        if not throw_prompt():
            break

def throw_prompt():
    reply = None 
    while True:
        reply = str(input(prompt)).lower().strip() 
        if reply not in ["y", "n"]:
            print("Input 'y' for yes or 'n' for no please")
            continue
        if reply[0] == "y":
            return True
        else:
            return False

dice_roller()
