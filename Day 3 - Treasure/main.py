def treasure_island():
    print("Welcome to Treasure Island")
    first_choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()
    if first_choice == "left":
        second_choice = input("What do you want to do? Type 'swim' or 'wait': ").lower()
        if second_choice == "wait":
            third_choice = input("Which door would you like to choose? Type 'red', 'blue' or 'yellow': ").lower()
            if third_choice == "yellow":
                print("You Win!")
            else:
                print("Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")

treasure_island()