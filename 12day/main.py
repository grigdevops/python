from art import logo
import random


print(logo)


continue_game = True
number_attempts = 0

random_number = random.randint(1,101)

def compare(try_number,rand_number):
    if try_number > rand_number:
        print("Too high")
    else:
        print("Too low")



print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Welcome to the Number Guessing Game!")
print(f"Pssst, the correct answer is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")



if difficulty == 'easy':
    number_attempts = 10
    print(f"You have {number_attempts} remaining to guess the number.")
    while continue_game:
        entered_number = int(input("Make a guess: "))
        if entered_number == random_number:
            continue_game = False
            print("You WIN!!!!")
        else:
            compare(entered_number, random_number)
            number_attempts -= 1
            print(f"You have {number_attempts}")
            if number_attempts == 0:
                continue_game = False
                print("You attempts expired Arraaaa")
elif difficulty == 'hard':
    number_attempts = 5
    print(f"You have {number_attempts} remaining to guess the number.")
    while continue_game:
        entered_number = int(input("Make a guess: "))
        if entered_number == random_number:
            continue_game = False
            print("You WIN!!!!")
        else:
            compare(entered_number, random_number)
            number_attempts -= 1
            print(f"You have {number_attempts}")
            if number_attempts == 0:
                continue_game = False
                print("You attempts expired Arraaaa")
else:
    print("You are entered wrong choice of difficulty")




