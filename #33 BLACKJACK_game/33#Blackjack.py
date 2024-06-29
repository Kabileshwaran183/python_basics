import random
from replit import clear
from cards import dict_cards,starting_logo,rules_1

card_list = [10,2,3,4,5,6,7,8,9,10,10,10,10,]
again_continue=True
while again_continue==True :
    print(starting_logo)
    print(rules_1)
    card_1 = random.choice(card_list)
    pos_card_1 = str(card_list.index(card_1) + 1) 
    card_2 = random.choice(card_list)
    pos_card_2= str(card_list.index(card_2) + 1)
    com_card_1 = random.choice(card_list)
    pos_com_card_1 = str(card_list.index(com_card_1) + 1)
    player_list = [card_1 , card_2]
    com_list = [com_card_1]
    print(f"You have : {player_list}")
    print(f"{dict_cards[pos_card_1]}    {dict_cards[pos_card_2]}")
    print(f"computer have : {com_list}")
    print(f"{dict_cards[pos_com_card_1]}")
    computer_choice="y"
    pos_list_player=[pos_card_1,pos_card_2]
    while input('Do you want next card : "y" or "n"')== "y" :
        player_extra_card = random.choice(card_list)
        pos_player_extra_card = [str(card_list.index(player_extra_card)+1)]
        pos_list_player+=pos_player_extra_card
        player_list.append(player_extra_card)
        print(f"You have : {player_list}")
        for i in pos_list_player:
            print(f"{dict_cards[i]}")
    pos_list_com=[pos_com_card_1]
    while computer_choice == "y":
        com_extra_card = random.choice(card_list)
        pos_com_extra_card = [str(card_list.index(com_extra_card)+1)]
        pos_list_com+=pos_com_extra_card
        com_list.append(com_extra_card)
        com_points = 0
        for i in com_list :        
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
    for i in player_list :    
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