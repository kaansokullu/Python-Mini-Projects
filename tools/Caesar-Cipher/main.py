import caesar_cipher_art

print(caesar_cipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for char in plain_text:
        alphabet_index = (alphabet.index(char) + shift_amount) % 26
        cipher_text += alphabet[alphabet_index]

    print("\n-----RESULT-----")
    print(f"The encrypted text is: {cipher_text}\n")

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print("\n-----RESULT-----")
    print(f"The decoded text is: {cipher_text}\n")

def cipher_caesar(plain_text, shift_amount, e_or_d):
    if e_or_d == "e":
        return encrypt(plain_text, shift_amount)
    else:
        return decrypt(plain_text, shift_amount)
    
while True:
    encode_or_decode = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher_caesar(text, shift, encode_or_decode)

    run_again = input("Type 'y' if you want to continue, otherwise 'n': ").lower()

    if run_again == "n":
        break