import random
def ask_to_play_again():
    play_again=input("Do you want to play again? Y or N :").lower()
    if play_again=='n':
        return is_play_again==False 
    
def guess(lives):
    print(f"TOTAL = {lives}lives")
    Actual_Number=random.randint(0,101)
    while(game_starts==True):
        Guessing_Number=int(input("Guess the number : "))
        if Guessing_Number==Actual_Number:
            print("Congratulation you won!!")
            ask_to_play_again()
            break
        else:
            if Guessing_Number<Actual_Number:
                print("low.Guess more high")
            elif Guessing_Number>Actual_Number:
                print("high.Guess more low")          
            else:
                print("Enter valid guess")
            lives-=1
            print(f"you have {lives} more lives")
            if lives==0:
                print("Game Over!")
                ask_to_play_again()
                break

is_play_again=True
while(is_play_again):
    game_starts=False
    level= input("enter the diffuculty level: easy or hard :")
    while(game_starts==False):
        if level == "easy":
            game_starts= True
            guess(10)
        elif level == "hard":
            game_starts= True
            guess(5)
        else:
            level=input('enter the valid opt:')