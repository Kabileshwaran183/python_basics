import random
is_play_again=True
while(is_play_again==True):
    game_starts=False
    level= input("enter the diffuculty level: easy or hard :").lower()
    while(game_starts==False):
        if level == "easy":
            lives=10
            game_starts= True
        elif level == "hard":
            lives=5
            game_starts= True
        else:
            level=input('enter the valid opt:')
    print(f"TOTAL = {lives}lives")
    Actual_Number=random.randint(0,101)
    while(game_starts==True):
        Guessing_Number=int(input("Guess the number : "))
        if Guessing_Number==Actual_Number:
            print("Congratulation you won!!")
            play_again=input("Do you want to play again? Y or N :").lower()
            if play_again=='n':
                is_play_again=False            
        else:
            if Guessing_Number<Actual_Number:
                print("low.Guess more high")
            elif Guessing_Number>Actual_Number:
                print("high.Guess more low")          
            else:
                print("Enter valid guess")
            print(f"you have {lives} more lives")
            lives-=1
        if lives==0:
            print("Game Over!")
