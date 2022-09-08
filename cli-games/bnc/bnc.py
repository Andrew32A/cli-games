from random import randint

# Had to rewrite the whole script to implement scoring, input checker, and tutorial. 

# Variables
roles = ["bear", "ninja", "cowboy"]
computer = roles[randint(0,2)].lower()
player = False
score = 0
spacing = "\n\n"

# Functions
def cowboy():
    # Global allows python to interpret score in functions
    global score
    if player == computer:
        print(f"{spacing}Draw!")
    elif computer == "bear":
        print(f"{spacing}You win!! Cowboy shoots bear")
        score += 1
    elif computer == "ninja":
        print(f"{spacing}You lose. Ninja is faster than cowboy")
        score -= 1

def bear():
    global score
    if player == computer:
        print(f"{spacing}Draw!")
    elif computer == "cowboy":
        print(f"{spacing}You lose. Cowboy shoots bear")
        score -= 1
    elif computer == "ninja":
        print(f"{spacing}You win!! Bear eats ninja")
        score += 1

def ninja():
    global score
    if player == computer:
        print(f"{spacing}Draw!")
    elif computer == "bear":
        print(f"{spacing}You lose. Bear eats ninja")
        score -= 1
    elif computer == "cowboy":
        print(f"{spacing}You win!! Ninja is faster than cowboy")
        score += 1

# Welcome message
print(f"Welcome to Bear Ninja Cowboy!{spacing}")

# Ask for rules
rules = input("Would you like the instructions for BNC? (Yes/No) > ").lower()
if rules == "yes":
    print(f"{spacing}Bear, Ninja, Cowboy is a lot like rock paper scissors!!{spacing}\nCowboy shoots Bear\nBear eats Ninja\nNinja is faster than Cowboy{spacing}")
else:
    print(f"{spacing}Starting game!{spacing}")

# Game loop
while player == False:
    player = input("Would you like to be Bear, Ninja, or Cowboy? > ").lower()

    if player == "cowboy":
        cowboy()
        print(f"Your score is now {score}!")
    elif player == "bear":
        bear()
        print(f"Your score is now {score}!")
    elif player == "ninja":
        ninja()
        print(f"Your score is now {score}!")
    else:
        print(f"{spacing}{player} is not a Bear, Ninja, or Cowboy. Please input a valid role.{spacing}")
        print(f"Your total score is {score}!")
        break


    player = False
    computer = roles[randint(0,2)]

    play_again = input(f"{spacing}Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
        player = False
        computer = roles[randint(0,2)]
    else:
        print(f"{spacing}Your total score is {score}!{spacing}Thanks for playing!!")
        break
