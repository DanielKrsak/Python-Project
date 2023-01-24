import random

computer_choice = random.randint(1, 3)


def rock_paper_scissors(computer):

    options = ["1", "2", "3"]
    while True:
        player_choice = input("Rock, paper or scissors? Type 1, 2 or 3: ")
        if player_choice not in options:
            print("Wrong input. Choose again.\n")
            continue
        else:
            player = int(player_choice)
            if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
                print(f"Player selected: {player}")
                print(f"Computer selected: {computer}")
                print("Player Wins!")
            elif (computer == 1 and player == 3) or (computer == 2 and player == 1) or (computer == 3 and player == 2):
                print(f"Player selected: {player}")
                print(f"Computer selected: {computer}")
                print("Computer Wins!")
            else:
                print(f"Player selected: {player}")
                print(f"Computer selected: {computer}")
                print("It's a Tie!")
            play_again = input("\nWould you like to play again? Type 'yes' or 'no': ").lower()
            if play_again == "yes":
                computer = random.randint(1, 3)
                continue
            else:
                print("Thank you for playing!")
                break


rock_paper_scissors(computer_choice)