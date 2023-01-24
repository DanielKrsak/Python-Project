import random

playing = True
player_cards = []
computer_cards = []


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_winner(player, computer):
    if sum(player) > 21:
        if 11 not in player:
            print(f"Your final hand: {player}\nComputer's final hand: {computer}\nComputer Wins!")
        else:
            get_index = player.index(11)
            player[get_index] = 1
    elif sum(computer) > 21:
        if 11 not in computer:
            print(f"Your final hand: {player}\nComputer's final hand: {computer}\nYou Win!")
        else:
            get_index = computer.index(11)
            computer[get_index] = 1
    else:
        if sum(player) > sum(computer):
            print(f"Your final hand: {player}\nComputer's final hand: {computer}\nYou Win!")
        elif sum(player) < sum(computer):
            print(f"Your final hand: {player}\nComputer's final hand: {computer}\nComputer Wins!")
        else:
            print(f"Your final hand: {player}\nComputer's final hand: {computer}\nIt's a Tie!")


while playing:
    for i in range(2):
        player_cards.append(draw_card())
        computer_cards.append(draw_card())

    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    choice = input("Type 'y' to get another card, or 'n' to pass: ")
    if choice == "n":
        calculate_winner(player_cards, computer_cards)
        break
    else:
        while True:
            player_cards.append(draw_card())
            if sum(computer_cards) < 17:
                computer_cards.append(draw_card())
            if sum(player_cards) <= 21:
                print(f"Your cards: {player_cards}")
                print(f"Computer's first card: {computer_cards[0]}")
                if input("Type 'y' to get another card, or 'n' to pass: ") == "y":
                    continue
                else:
                    calculate_winner(player_cards, computer_cards)
                    playing = False
                    break
            else:
                calculate_winner(player_cards, computer_cards)
                playing = False
                break

