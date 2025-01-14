alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text :
        pos = alphabet.index(letter)
        new_pos = (pos+shift_amount)%26
        new_letter = alphabet[new_pos]
        cipher_text += new_letter

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        pos = alphabet.index(letter)
        new_pos = (pos+shift_amount)%26
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        pos = alphabet.index(letter)
        new_pos = (pos-shift_amount)
        new_letter = alphabet[new_pos]
        plain_text += new_letter
    print(f"The encoded text is {plain_text}")

if direction == "encode" :
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode" :
    decrypt(cipher_text=text,shift_amount=shift)
else:
    print("Enter the correct option.")