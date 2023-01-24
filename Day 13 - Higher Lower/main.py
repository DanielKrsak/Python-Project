from data import data
import random

game_data = data
still_playing = 2
score = 0


def select_celeb(celeb):
    random_celeb = random.choice(celeb)
    return random_celeb


def make_comparison(celeb1, celeb2, player):
    if celeb1 > celeb2 and player == "a":
        print("\nYou're right!")
        return True
    elif celeb1 < celeb2 and player == "b":
        print("\nYou're right!")
        return True
    else:
        return False


celeb_list = [select_celeb(game_data) for i in range(2)]
used_list = []


while still_playing <= len(game_data):
    if celeb_list[0] not in used_list or celeb_list[1] not in used_list or celeb_list[0] != celeb_list[1]:
        print(f"Compare A: {celeb_list[0]['name']}, a {celeb_list[0]['description']}, from {celeb_list[0]['country']}\n")
        print("VERSUS\n")
        print(f"Compare B: {celeb_list[1]['name']}, a {celeb_list[1]['description']}, from {celeb_list[1]['country']}\n")

        choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if choice == "a" or choice == "b":
            if make_comparison(celeb_list[0]["follower_count"], celeb_list[1]["follower_count"], choice):
                used_list.append(celeb_list[0])
                celeb_list.pop(0)
                celeb_list.append(select_celeb(game_data))
                score += 1
                still_playing += 1
            else:
                print(f"Sorry, that's wrong! Final score: {score}")
                break
        else:
            print("Wrong input! Try again.\n")
            continue

    else:
        celeb_list = [select_celeb(game_data) for i in range(2)]
