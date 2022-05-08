from ast import Or
import time
import button as buttons
import dc as dc
import ThomasStabileKode as stepper

player_count = 0
max_player_count = 3
max_turn = 90
player_positions = []
card_spacing = 2
rpm = 2
sleep_duration = 0.5

while True:

    #Player count
    while buttons.button_2() == False or player_count == max_player_count: #If button 2 or max number of players is reached, skip
        if buttons.button_1():
            player_count +=1
            time.sleep(sleep_duration)
    
    #Generate player positions 
    for x in range(player_count):
        player_positions.append(0-(max_turn/2) + (max_turn/player_count)*x +(max_turn/(player_count*2)))

    #Deal first card to dealer
    stepper.go_to_pos(0, rpm)
    dc.d_card()

    #Loop through players
    for player in range(player_count):
        stepper.go_to_pos(player_positions[player], rpm)
        standing = False

        #Deal card if player presses 'Button 1', proceed to next player if 'Button 2' is pressed
        while(standing == False):
            if buttons.button_1:
                stepper.go_to_pos(player_positions[player], rpm)
                dc.p_card()
                player_positions[player] += card_spacing
            elif buttons.button_2:
                standing = True
            time.sleep(sleep_duration)
    #Deal first card to dealer
    stepper.go_to_pos(0, rpm)
    dc.d_card()
            
    #Code for registering dealer cards

