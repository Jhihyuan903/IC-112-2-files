#h24124042統計系黃稚元
def player_cards(deck):
    player_hand = [deck.pop(0), deck.pop(0)]
    return player_hand
def dealer_cards(deck):
    dealer_hand = [deck.pop(0), deck.pop(0)]
    return dealer_hand

import random
rank=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits=["Spade","Heart","Diamond","Club"]#"spade","heart","diamond","club"
deck=[]#store a deck of cards

#create a deck of cards
for i in range(len(rank)):
    for j in range(len(suits)):
        deck.append(rank[i]+"-"+suits[j])
random.shuffle(deck)

player_hand=player_cards(deck)#drawing a hand of cards for player
dealer_hand=dealer_cards(deck)#drawing a hand of cards for dealer
#sum of the cards in hand
value_sum=0
for i in range(2):
    card=player_hand[i]
    card.split("-")
    if card[0:2]=="10" or card[0] == "J" or card[0] == "Q" or card[0] == "K":
        card_value = 10
    elif card[0]=="A":
        card_value=11
    else:
        card_value=int(card[0])
    value_sum+=card_value
result=" ".join(player_hand)#list->str
print("Your current value is ",value_sum)
print("with the hand: ",result)

while True:
    n=int(input("Hit or Stay? (hit=1,stay=0):"))
    if n==1:
        draw_card=deck.pop(0)
        print("You draw ",draw_card)
        draw_card.split("-")
        if (draw_card[0:2]=="10" or draw_card[0] == "J" or draw_card[0] == "Q" or draw_card[0] == "K"):
            draw_card_value = 10
        elif draw_card[0]=="A":
            if value_sum<=10:
                draw_card_value=11
            else:
                draw_card_value=1
        else:
            draw_card_value=int(card[0])
        value_sum+=draw_card_value
        if value_sum==21:
            player_hand.append(draw_card)
            result=" ".join(player_hand)#list->str
            print("Your current value is Blackjack!(21)")
            print("with the hand: ",result)
            break
        elif value_sum>21:
            player_hand.append(draw_card)
            result=" ".join(player_hand)#list->str
            print("Your current value is bust(>21)")
            print(print("with the hand: ",result))
            break
        else:
            player_hand.append(draw_card)
            result=" ".join(player_hand)#list->str
            print("Your current value is ",value_sum)
            print("with the hand: ",result)
    
    else:
        break