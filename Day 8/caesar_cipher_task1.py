alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]  # 25

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift):

    new_alpha = []
    j = shift
    for i in range(26):
        new_alpha.append(alphabet[j])
        if j == (len(alphabet) - 1):  # last index
            j = 0
        else:
            j += 1

    print(new_alpha)
    # ------------------------------------
    cipher_text = ""
    for char in plain_text:
        i = alphabet.index(char)
        cipher_text += str(alphabet[i + shift])

    print(f"The encoded text is {cipher_text}")


encrypt(text, shift)
