print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1=input('you\'re at cross road.What way did you choose : "left" or "right"').lower()
if (choice1=="right") :
    choice2=input('you\'ve come to lake.There is an island in the middle of lake.Type "wait" to wait boat.Type "swim" to swim across the river.').lower()
    if (choice2=="wait"):
        choice3=input('You\'ve come to the island by the boat.open the correct door by choosing the color "red" "yellow" "blue": ').lower()
        if (choice3=="red"):
            print("The room is full of fire. GAMEOVER!!!")
        elif choice3=="yellow":
            print("You find the treasure. YOU WIN!!!")
        elif choice3=="blue":
            print("The room is full of ice. GAMEOVER!!!")
        else:
            print("The choosen door is not found.GAMEOVER!!!")
    else:
        print("you are sink into the lake.GAME OVER!!!")
else :
    print("you fell into the river.GAME OVER!!!")