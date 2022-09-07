# Importing json library
import json
from random import randint

# Variables for deck
game = True
score = 0
replay = ""
me_Capitals = "me-capitals.json"
math = "math.json"
science = "science.json"
spacing = "\n\n\n\n"

# Beginning of loop
while game == True:
    # Deck selector
    deck = input("What would you like to be quizzed on? (Capitals, math, or science) > ").lower()
    if deck == "capitals":
        deck = me_Capitals
    elif deck == "math":
        deck = math
    elif deck == "science":
        deck = science
    else:
        print(f"{spacing}Please run program again and enter a valid name.{spacing}")
        break

    # Opens and reads (fr for read) json file
    with open((deck), 'r') as f:
        data = json.load(f)

    # Length of card array stored in 'total' variable
    total = len(data["cards"])

    for i in data["cards"]:
        guess = input(i["q"] + " > ").lower()

        if guess == i["a"]:
            # +1 Score counter
            score += 1
            # Add score and total into the response
            print(f"Correct! Current score: ({score}/{total})")
        else:
            print("Incorrect! The correct answer was", i["a"])
            print(f"Current score: ({score}/{total})")

    # Final score output and message
    print(spacing)
    if score == 5:
        print(f"Wow!! You are amazing! You got all of them correct! ({score}/{total})")
    elif score == 4:
        print(f"Good Job! ({score}/{total})")
    elif score == 3:
        print(f"Not bad! ({score}/{total})")
    elif score == 2:
        print(f"Could use some improvement. ({score}/{total})")
    elif score == 1:
        print(f"Well... at least you got one! ({score}/{total})")
    elif score == 0:
        print(f"Better luck next time. ({score}/{total})")

    # Replay loop
    print("\n\n\n\n")
    replay = input("Would you like to play again? (Yes/No) > ").lower()
    if replay == "yes":
        print(f"{spacing}Loading next round!{spacing}")
    else:
        print(f"{spacing}Thank you for playing!!{spacing}")
        break