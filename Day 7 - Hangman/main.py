from words import words
import random
import string


def get_valid_word(words):
    random_word = random.choice(words)
    while "-" in random_word or " " in random_word:
        random_word = random.choice(words)

    return random_word.upper()


def hangman():
    word = get_valid_word(words)
    lives = 10

    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while True:
        print(f"You have used following letters:", ", ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(" ".join(word_list))

        user_input = input("Type something: ").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print(f"Wrong. You have {lives} lives remaining.")

        elif user_input in used_letters:
            print("You have already used this letter.")

        else:
            print("Invalid character.")

        if word_letters.issubset(used_letters):
            print(f"Congrats. You guessed the word {word.upper()}")
            break
        elif lives == 0:
            print("You ran out of lives.")
            break

hangman()