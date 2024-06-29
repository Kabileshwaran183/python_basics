alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue=True
while should_continue:
    wrong_input = True
    while wrong_input:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if not (direction =="encode" or direction =="decode") :
            print("Enter the valid option")
        else:
            wrong_input=False
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceasar(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text :
            if letter in alphabet :
                pos = alphabet.index(letter)
                if direction == "encode" :
                    new_pos = (pos+shift_amount)%26
                elif direction == "decode" :
                    new_pos = (pos-shift_amount)%26
                new_letter = alphabet[new_pos]
                cipher_text += new_letter
            else:
                cipher_text+=letter
        print(f"The resulted text is : {cipher_text}")
    ceasar(plain_text=text,shift_amount=shift)
    result = input('If you want to continue,type "yes" or else type "no"  : ').lower()
    wrong=True
    while wrong:
        if not (result =="yes" or "no"):
            print("Enter the correct choice")
        else:
            wrong=False
            if result == "no":
                should_continue=False
                print("Good Bye")