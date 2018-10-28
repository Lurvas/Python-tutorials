import random

msg_welcome = "Welcome to Guess The Number!\nPlease input in what interval you want to guess." 

def main():
    while True:
        print(msg_welcome)
        try:
            start = int(input("Input starting number:\n"))
            end = int(input("Input end number:\n"))
            choosen_number = random_number(start, end)
            print(choosen_number)
            guess = input("A number between " + str(start - 1) + " and " + str(end + 1) + " has been choosen, it's time to guess:\n")
        except ValueError:
            print("Input must be a number!") 
             

#Define function that generate a number between a and b
def random_number(a, b):
    rand_int = random.randint(a, b)
    return rand_int

def check_number(choosen_number, guess):
    if guess == choosen_number:
        return True
    elif guess < choosen_number:
        print("Your guess was to low, try again!")
        return False
    elif guess > choosen_number:
        print("Your guess was to high, try again!")
        return False

if __name__ == "__main__":
    main()
