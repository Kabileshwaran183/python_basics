alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text :
        pos = alphabet.index(letter)
        if direction == "encode" :
            new_pos = (pos+shift_amount)%26
        elif direction == "decode" :
            new_pos = (pos-shift_amount)%26
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    print(f"The resulted text is : {cipher_text}")
ceasar(plain_text=text,shift_amount=shift)
