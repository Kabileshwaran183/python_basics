import random

def guessing(max,balance_attempts):
    attempts = 0
    msg = ""
    should_continue = True
    while should_continue and attempts < max:
        print(f"You have {balance_attempts} attempts more")
        guess = int(input("Make a guess: "))
        if guess == given_number :
            msg = "You got the number."
            should_continue = False
            print(msg)
        else :
            if guess < given_number :
                msg = "low"
            else :
                msg = "high"
            print(msg)
            attempts += 1
            balance_attempts-=1
    if should_continue == True:
        print("You have lost all your attempts")
        
def easy():
    guessing(max= 10,balance_attempts = 10)

def hard():
    guessing(max= 5, balance_attempts =5)

play_again = True
while play_again :      
    print('''//   _   _ _   ____  ________ ___________   _____ _   _ _____ _____ _____ _____ _   _ _____  
    //  | \ | | | | |  \/  | ___ |  ___| ___ \ |  __ | | | |  ___/  ___/  ___|_   _| \ | |  __ \ 
    //  |  \| | | | | .  . | |_/ | |__ | |_/ / | |  \| | | | |__ \ `--.\ `--.  | | |  \| | |  \/ 
    //  | . ` | | | | |\/| | ___ |  __||    /  | | __| | | |  __| `--. \`--. \ | | | . ` | | __  
    //  | |\  | |_| | |  | | |_/ | |___| |\ \  | |_\ | |_| | |___/\__/ /\__/ /_| |_| |\  | |_\ \ 
    //  \_| \_/\___/\_|  |_\____/\____/\_| \_|  \____/\___/\____/\____/\____/ \___/\_| \_/\____/ 
    //                                                                                           
    //                                                                                           ''')
    given_number = random.randint(1,101)

    wrong_option=True
    while wrong_option :
        difficulty=input("Enter the difficulty level (easy or hard) : ").lower()
        if difficulty == "easy" :
            wrong_option=False
            easy()
        elif difficulty == "hard" :
            wrong_option=False
            hard()
        else :
            print("Enter the valid option") 
    if input('Do you want to play again? ("y" or "n") : ').lower() == "n" :
        play_again=False
        print("GOOD BYE")


