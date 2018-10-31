import random
import sys

msg_welcome = "\nWelcome to Guess The Number!\nPlease input in what interval you want to guess." 

def main():
    print(msg_welcome)
    while True:
        start = start_number()
        end = end_number()        
        if start > end:
            print("The starting number must be smaller the ending number. Try again!")
            return main()
        else:
            choosen_number = random_number(start, end)
#            print(choosen_number)
            print("A number between " + str(start -1) + " and " + str(end + 1) + " has been choosen, it's time to make your first guess!")
            while True:
                try:
                    guess = int(input())
                    check_number(choosen_number, guess)
                except ValueError:
                    print("Input must be a number!") 

#Define function that generate a number between a and b
def random_number(a, b):
    rand_int = random.randint(a, b)
    return rand_int

def start_number():
    start = None
    while True:
        try:
            start = int(input("Input starting number:\n"))
            return start
        except ValueError:
            print("Input must be a whole number!")
            continue
            
def end_number():
    end = None
    while True:
        try:
            end = int(input("Input end number:\n"))
            return end
        except ValueError:
            print("Input must be a whole number!")
            continue

def check_number(choosen_number, guess):
    if guess == choosen_number:
        print("\nCongratulations! Your guess was correct!")
        return play_again()
    elif guess < choosen_number:
        print("Your guess was to low, try again!")
        return False
    elif guess > choosen_number:
        print("Your guess was to high, try again!")
        return False

def play_again():
    reply = None
    print("Do you wanna play again? [Y/n]\n")
    while True:
        reply = str(input()).lower().strip()
        if reply not in ["y", "n"]:
            print("Input 'y' for yes or 'n' for no please.")
            continue
        if reply[0] == "y":
            return main()
        else:
            sys.exit()

if __name__ == "__main__":
    main()
