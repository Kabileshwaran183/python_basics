from HMlogo import word_list,stages,logo
import random
print(logo)
chosen_word = random.choice(word_list)
display=[]
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
end_of_game=False
lives=6
while not end_of_game:
    print(f"you have {lives} life yet.")
    guess = input("guess the word:").lower()
    if guess in display:
        print("this letter is already guessed ")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess :
                display[position] = letter
        print(display)
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not in the word, you lose 1 life!")
            if lives == 0:
                end_of_game=True
                print("You lose")
        if '_' not in display:
            end_of_game=True
            print("you win.")
        print(stages[lives])
