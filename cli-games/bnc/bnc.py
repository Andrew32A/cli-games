from random import randint

roles = ["bear", "ninja", "cowboy"]
computer = roles[randint(0,2)].lower()
player = False
spacing = "\n\n\n\n"

while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ").lower()
    
    if player != "bear" or "ninja" or "cowboy" or False:
      print(f"{spacing}{player} is not a Bear, Ninja, or Cowboy. Please input a valid role.{spacing}")

    # Compare computer and player role
    if computer == player:
      print("DRAW!")
    
    elif computer == "cowboy":
      if player == "bear":
        print("You lose!", computer.capitalize(), "shoots", player.capitalize())
      else: # computer is cowboy, player is ninja
        print("You win!", player.capitalize(), "defeats", computer.capitalize())
    elif computer == "bear":
      if player == "cowboy":
        print("You win!", player.capitalize(), "shoots", computer.capitalize())
      else: # computer is bear, player is ninja
        print("You lose!", computer.capitalize(), "eats", player.capitalize())
    elif computer == "ninja":
      if player == "cowboy":
        print("You lose!", computer.capitalize(), "defeats", player.capitalize())
      else: # computer is ninja, player is bear
        print("You win!", player.capitalize(), "eats", computer.capitalize())
    

      player = False
      computer = roles[randint(0,2)]

    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break