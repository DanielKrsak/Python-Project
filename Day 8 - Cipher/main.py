alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode_decode(method, message, shift, final_word=""):
    if method == "encode":
        for i in message:
            for y in alphabet:
                if i == y:
                    get_index = alphabet.index(y)
                    if get_index + shift >= len(alphabet):
                        final_word += alphabet[get_index + shift - len(alphabet)]
                    else:
                        final_word += alphabet[get_index + shift]
    else:
        if method == "decode":
            for i in message:
                for y in alphabet:
                    if i == y:
                        get_index = alphabet.index(y)
                        if get_index - shift < 0:
                            final_word += alphabet[get_index - shift + len(alphabet)]
                        else:
                            final_word += alphabet[get_index - shift]
    print(final_word)


while True:
    user_method = input("Encode or Decode?: ").lower()
    user_message = input("Type your message: ").lower()
    user_shift = int(input("Type your shift number: "))

    encode_decode(user_method, user_message, user_shift)

    go_again = input("Would you like to go again? ").lower()

    if go_again == "yes":
        continue
    else:
        break
