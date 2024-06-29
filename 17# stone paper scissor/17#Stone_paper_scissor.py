import random
stone=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)______
           _________)
          ___________)
          _________)
---. ___________)
""")

scissor=("""
    _______
---'   ____)______
          _________)
       _____________)
      (____)
---.__(___)
""")
for i in range(5):
  select=int(input("What do you choose?\n 0 for stone\n 1 for paper\n 2 for scissor  "))
  computer_hand=random.randint(0,2)
  print("COMPUTER")
  if (computer_hand==0):
    print(stone)
  elif (computer_hand==1):
    print(paper)
  elif (computer_hand==2):
    print(scissor)
  print("YOU") 
  if (select==0):
    print(stone)
  elif (select==1):
    print(paper)
  elif (select==2):
    print(scissor)
  else:
    print("Enter the valid option")
  if (computer_hand==0 and select==1):
    print("YOU WIN!!")
  elif (computer_hand==1 and select==2):
    print("YOU WIN!!")
  elif (computer_hand==0 and select==2):
    print("COMPUTER WIN!!")
  elif (computer_hand==1 and select==0):
    print("COMPUTER WIN!!")
  elif (computer_hand==2 and select==0):
    print("YOU WIN!!")
  elif (computer_hand==2 and select==1):
    print("COMPUTER WIN!!")
  else :
    print("DRAW!!")
  print("**************************************************\n")  