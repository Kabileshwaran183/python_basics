word_list= ['adventure','automatic','creation']
import random
chosen_word = random.choice(word_list)
guess = input("guess the word:").lower()

display=[]
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess :
        display[position] = letter
print(display)
print(chosen_word)