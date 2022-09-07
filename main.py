alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1:

def encode(text_input, shift_space):
    t1 = ""
    for i in text_input:
        position = alphabet.index(i)

        new_position = position + shift_space

        t1 += alphabet[new_position]

    print(t1)


# TODO-2:

def decode(text_input, shift_space):
    t2 = ""
    for i in text_input:
        position = alphabet.index(i)

        new_position = position - shift_space

        t2 += alphabet[new_position]

    print(t2)


# TODO-3:

game_on = True

while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt and Exit to end:\n")

    if direction == "exit":
        game_on = False

    elif direction == "encode":

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26

        encode(text_input=text, shift_space=shift)

    elif direction == "decode":

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26

        decode(text_input=text, shift_space=shift)
