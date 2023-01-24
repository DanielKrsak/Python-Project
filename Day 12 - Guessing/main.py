import random

print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100")

lives = 0
random_number = random.randint(1, 100)
user_choice = 0


def check_answer(user_choice, random_number, lives):
    if user_choice > random_number:
        lives -= 1
        print(f"Too high! {lives} remaining.")
        return lives
    elif user_choice < random_number:
        lives -= 1
        print(f"Too low! {lives} remaining.")
        return lives
    else:
        print(f"You guessed it! Correct number was {random_number}.")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    lives = 10
    print(f"You have {lives} attempts remaining to a guess a number.")
else:
    lives = 5
    print(f"You have {lives} attempts remaining to a guess a number.")

while user_choice != random_number:
    if lives > 0:
        user_choice = int(input("Make a guess: "))
        lives = check_answer(user_choice, random_number, lives)
    else:
        print(f"You lose! Correct number was {random_number}.")
        break