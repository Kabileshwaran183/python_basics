import random

dict_cards={
"13": '''.------.
|K     |
|      |
|     K|
'------"''',
"12":'''.------.
|Q     |
|      |
|     Q|
'------"''',
"11":'''.------.
|J     |
|      |
|     J|
'------"''',
"1":'''.------.
|A     |
|      |
|     A|
'------"''',
"10":'''.------.
|10    |
|      |
|    10|
'------"''',
"9": '''.------.
|9     |
|      |
|     9|
'------"''',
"8":'''.------.
|8     |
|      |
|     8|
'------"''',
"7":'''.------.
|7     |
|      |
|     7|
'------"''',
"6":'''.------.
|6     |
|      |
|     6|
'------"''',
"5": '''.------.
|5     |
|      |
|     5|
'------"''',
"4":'''.------.
|4     |
|      |
|     4|
'------"''',
"3":'''.------.
|3     |
|      |
|     3|
'------"''',
"2":'''.------.
|2     |
|      |
|     2|
'------"'''}

starting_logo = '''▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
████░▄▄▀██░████░▄▄▀██░▄▄▀██░█▀▄█████░█░▄▄▀██░▄▄▀██░█▀▄████░▄▄░█░▄▄▀██░▄▀▄░██░▄▄
████░▄▄▀██░████░▀▀░██░█████░▄▀██████░█░▀▀░██░█████░▄▀█████░█▀▀█░▀▀░██░█░█░██░▄▄▄
████░▀▀░██░▀▀░█░██░██░▀▀▄██░██░██░▀▀░█░██░██░▀▀▄██░██░████░▀▀▄█░██░██░███░██░▀▀▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
'''
rules = '''
.-----------------------------------------------------------.
| RULES :
       1. Who having the greatest point is the winner.
       2. The MAX POINT is 21
          (ie: Taking more than 21 points,
               whose points are being burst.)
       3. Each card should have the seperate points.
          (ie: Number card has its own number as point
               A,J,Q,K -- 10 Points)  |
'--------------------------------------------------------'
'''

rules_1='''(¯`·¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸·´¯)
( \                                                                          / )
 ( ) RULES :
       1. Who having the greatest point is the winner.
       2. The MAX POINT is 21
          (ie: Taking more than 21 points,
               whose points are being burst.)
       3. Each card should have the seperate points.
          (ie: Number card has its own number as point
               A,J,Q,K -- 10 Points)  ( ) 
  (/                                                            \)  
   (.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`)   
'''
card_list = [[1,11],2,3,4,5,6,7,8,9,10,10,10,10,]
display_card = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
again_continue=True
while again_continue==True :
    print(starting_logo)
    print(rules_1)
    card_1 = random.choice(display_card)
    card_1_index = display_card.index(card_1)
    card_1_int  =card_list[card_1_index]
    pos_card_1 = str(card_1_index + 1)
    card_2 = random.choice(display_card)
    card_2_index = display_card.index(card_2)
    card_2_int = card_list[card_2_index]
    pos_card_2= str(card_2_index + 1)
    if card_1_index == 0:
        card_1_int = card_1_int[1]
        if card_2_index == 0:
            card_2_int = card_2_int[0]
    else :
        if card_2_index == 0:
            card_2_int = card_2_int[1] 
    com_card_1 = random.choice(display_card)
    com_card_1_index = display_card.index(com_card_1)
    com_card_1_int = card_list[com_card_1_index]
    pos_com_card_1 = str(com_card_1_index + 1)
    if com_card_1_index == 0 :
        com_card_1_int = com_card_1_int[1]
    player_list = [card_1 , card_2]
    player_list_int = [card_1_int , card_2_int]
    com_list = [com_card_1]
    com_list_int = [com_card_1_int]
    print(f"You have : {player_list}")
    print(f"{dict_cards[pos_card_1]}    {dict_cards[pos_card_2]}")
    print(f"computer have : {com_list}")
    print(f"{dict_cards[pos_com_card_1]}")
    computer_choice="y"
    pos_list_player=[pos_card_1,pos_card_2]
    while input('Do you want next card : "y" or "n"')== "y" :
        player_extra_card = random.choice(display_card)
        player_extra_card_index = display_card.index(player_extra_card)
        player_extra_card_int = card_list[player_extra_card_index]
        pos_player_extra_card = [str(player_extra_card_index+1)]
        if player_extra_card_index == 0:
            if card_1_index == 0 or card_2_index == 0 :
                player_extra_card_int = player_extra_card_int[0]
            else:
                player_extra_card_int = player_extra_card_int[1]
        pos_list_player+=pos_player_extra_card
        player_list.append(player_extra_card)
        player_list_int.append(player_extra_card_int)
        print(f"You have : {player_list}")
        for i in pos_list_player:
            print(f"{dict_cards[i]}")
    pos_list_com=[pos_com_card_1]
    while computer_choice == "y":
        com_extra_card = random.choice(display_card)
        com_extra_card_index = display_card.index(com_extra_card)
        com_extra_card_int = card_list[com_extra_card_index]
        pos_com_extra_card = [str(com_extra_card_index+1)]
        if com_extra_card_index == 0:
            com_extra_card_int = com_extra_card_int[1]
        pos_list_com+=pos_com_extra_card
        com_list.append(com_extra_card)
        com_list_int.append(com_extra_card_int)
        com_points = 0
        for i in com_list_int :     
            com_points += i
        if com_points<12 :
            computer_choice="y"
        elif com_points>18:
            computer_choice="n"
        elif com_points<14:
            computer_choice= random.choice(["y","y","y","y","n"])
        elif com_points<16:
            computer_choice= random.choice(["y","y","n","n"])
        elif com_points<18:
            computer_choice= random.choice(["y","n","n","n"])
    print((f"computer have : {com_list}"))
    for i in pos_list_com:
        print(f"{dict_cards[i]}")
    print(f"You have : {player_list}")
    for i in pos_list_player:
        print(f"{dict_cards[i]}")
    player_points = 0
    for i in player_list_int :
        player_points += i
    print("\n\t**********POINTS LIST**********")
    print(f"\t  you have {player_points} points")
    print(f"\t Computer have {com_points} points")
    print("\t*******************************")
    if player_points > 21 and com_points > 21 :
        print("\t  Your points were burst.")
        print("\t Computer points were burst.")
        print("\t*********draw match*********")
    if player_points > 21 :
        print("\t  Your points were burst.")
        print("\t*********Computer wins*********")
    elif com_points > 21 :
        print("\t Computer points were burst.")
        print("\t***********you wins***********")
    else :
        if player_points == com_points:
            print("\t*********draw match*********")
        elif player_points < com_points :
            print("\t*********Computer wins*********")
        else:
            print("\t***********you wins***********")
    print("\t*******************************")
    rematch=input('Do you want to play again:"y" or "n"')
    if rematch == "n":
        again_continue = False
    else:
        clear()