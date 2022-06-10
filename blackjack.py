from ast import Or
import time
import button as buttons
import dc as dc
import ThomasStabileKode as stepper
import carddetection as cd
import numpy as np

player_count = 0
max_player_count = 3
max_turn = 90
player_positions = np.zeros[max_player_count]
player_cards = []
card_spacing = 2
rpm = 2
sleep_duration = 0.5
next_card = 0
dealer_card = 0

while True:
    next_card = cd.get_card_value()

    #Player count
    while buttons.button_2() == False or player_count == max_player_count: #If button 2 or max number of players is reached, skip
        if buttons.button_1():
            player_count +=1
            time.sleep(sleep_duration)
    
    #Generate player positions 
    for x in range(player_count):
        player_positions.append(0-(max_turn/2) + (max_turn/player_count)*x +(max_turn/(player_count*2)))
    print(player_positions)
    
    #Deal 2 cards
    for x in range(2):
        for player in range(player_count):
            stepper.go_to_pos(player_positions[player], rpm)
            player_cards[player] += next_card
            dc.p_card()
            next_card = cd.get_card_value()
        if x == 0:
            #Deal first card to dealer
            stepper.go_to_pos(0, rpm)
            dealer_card += next_card
            dc.d_card()
            next_card = cd.get_card_value()
    
    
    #Loop through players
    for player in range(player_count):
        stepper.go_to_pos(player_positions[player], rpm)
        standing = False

        #Deal card if player presses 'Button 1', proceed to next player if 'Button 2' is pressed
        while(standing == False and player_cards[player] <21):
            if buttons.button_1():
                stepper.go_to_pos(player_positions[player], rpm)

                player_cards[player] += next_card
                dc.p_card()
                next_card = cd.get_card_value()

                player_positions[player] += card_spacing
            elif buttons.button_2():
                standing = True
            time.sleep(sleep_duration)
            
    #Deal cards to dealer
    stepper.go_to_pos(0, rpm)
    while dealer_card<17:
        dealer_card += next_card
        dc.d_card()
        next_card = cd.get_card_value()
