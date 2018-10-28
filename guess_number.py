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
            gueuss = input("A number between " + str(start - 1) + " and " + str(end + 1) + " has been choosen, it's time to guess:\n")
        except ValueError:
            print("Input must be a number!")
             

#Define function that generate a number between a and b
def random_number(a, b):
    rand_int = random.randint(a, b)
    return rand_int

if __name__ == "__main__":
    main()
