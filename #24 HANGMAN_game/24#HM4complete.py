stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list= ['adventure','automatic','creation']
import random
chosen_word = random.choice(word_list)
display=[]
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
end_of_game=False
lives=6
while not end_of_game:
    guess = input("guess the word:").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess :
            display[position] = letter
    print(stages[lives])
    print(display)
    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game=True
        print("You lose")
    if '_' not in display:
        end_of_game=True
        print("you win.")
