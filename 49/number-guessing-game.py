from random import randint


def input_num(graniza):
    def is_valid(num):
        return 0 < num <= graniza

    while True:
        try:
            num = int(input(f"Enter a number in range 1 - {graniza}: "))
            if is_valid(num):
                return num
            else:
                print(f"Please enter an integer between 1 and {graniza}.")
        except ValueError:
            print("Please enter a valid integer.")

def game():
    try_counter = 0
    print("Do you want to specify the upper limit? \nNo - n, Yes - enter the limit")
    graniza_input = input()
    if graniza_input.isdigit():
        graniza = int(graniza_input)
    else:
        graniza = 100
    magic_num = randint(1, graniza)
    print(f"I have guessed a number. \nTry to guess it (between 1 and {graniza})!")

    while True:
        user_num = input_num(graniza)
        if user_num < magic_num:
            print("Too low... Try again!")
            try_counter += 1
        elif user_num > magic_num:
            print("Too high! Try a smaller number.")
            try_counter += 1
        else:
            print("\nYou guessed it, congratulations!")
            break
    print(f"Number of attempts: {try_counter + 1}")




print("Welcome to the number guessing game!\n")
game()
print("Thank you for playing the number guessing game. \nSee ya again...")
