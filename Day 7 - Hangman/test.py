word = "Goodbye"
chosen_word = set(word.upper())
print(chosen_word)

used_letter = ["E", "D", "G", "O", "Y", "B", "G", "X", "Y", "Z"]
if chosen_word.issubset(used_letter):
    print("yes")