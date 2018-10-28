import random

msg_welcome = "Welcome to Guess The Number!\nPlease input in what interval you want to guess." 

def main():
    while True:
        print(msg_welcome)
        start = input("Input starting number:\n")
        end = input("Input end number:\n")
        choosen_number = random_number(start, end)
        print(choosen_number)
        guess = input("A number between " + str(start) + " and " + str(end) + "has been choosen, it's time to guess:\n")
        

#Define function that generate a number between a and b
def random_number(a, b):
    rand_int = random.randint(a, b)
    return rand_int

if __name__ == "__main__":
    main()
