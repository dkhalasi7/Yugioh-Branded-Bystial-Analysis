import random

def count_cards(deck):
    return len(deck)

def remove_card(hand, card_to_remove):
    hand = [card for card in hand if card != card_to_remove]
    return hand

def check_card_count(hand, card):
    return hand.count(card)

def generate_hands(deck, num_hands, hand_size):
    hands = []
    for i in range(num_hands):
        hand = random.sample(deck, hand_size)
        hands.append(hand)
    return hands

def light_dark_check(hand):
    light_dark_monsters = ["Aluber The Jester of Despia",   
    "Fallen of Albaz", "Despian Tragedy",    
    "Edge Imp Chain", "Dramaturge of Despia",    "Ad Libitum of Despia",    
    "The Bystial Lubellion", 
    "Bystial Magnamhut", "Bystial Saronir",    
    "Bystial Druiswurm", "Albion the Shrouded Dragon", "Tri-Brigade Mercourier", 
    "Blazing Cartesia, the Virtuous"]
    
    for card in hand:
        if card in light_dark_monsters:
            return True
    
    return False

def allure_adjust(hand, deck):
    albion_activated = False
    while("Allure of Darkness" in hand):
        regained_activated = False
        for card in hand:
            deck = remove_card(deck, card) # removing cards from deck
        
        if("Branded Regained" in hand):
            hand = remove_card(hand, "Branded Regained") #activating branded regained
            regained_activated = True
        
        hand = remove_card(hand, "Allure of Darkness")
        draws = generate_hands(deck, 1, 2)

        for card in draws[0]:
            hand.append(card)
            deck = remove_card(deck,card)
                
        if("Despian Tragedy" in hand):
            hand = remove_card(hand, "Despian Tragedy")
            if("Aluber The Jester of Despia" not in hand):
                hand.append("Aluber The Jester of Despia")
                deck = remove_card(deck, "Aluber The Jester of Despia")
            elif("Dramaturge of Despia" not in hand and "Dramaturge of Despia" in deck):
                hand.append("Dramaturge of Despia")
                deck = remove_card(deck, "Dramaturge of Despia")
            elif("Ad Libitum of Despia" not in hand and "Ad Libitum of Despia" in deck):
                hand.append("Ad Libitum of Despia")
                deck = remove_card(deck, "Ad Libitum of Despia")
            elif(check_card_count(hand,"Aluber The Jester of Despia") != 3):
                hand.append("Aluber The Jester of Despia")
                deck = remove_card(deck, "Aluber The Jester of Despia")
            
            if(regained_activated):
                draw = generate_hands(deck,1,1)
                deck.append("Despian Tragedy")
                for card in draw[0]:
                    hand.append(card)
                    deck = remove_card(deck,card)

        elif ("Tri-Brigade Mercourier" in hand):
            hand = remove_card(hand, "Tri-Brigade Mercourier")
            if("Albion the Shrouded Dragon" not in hand and albion_activated == False and "Albion the Shrouded Dragon" in deck):
                hand.append("Albion the Shrouded Dragon")
                deck = remove_card(deck,"Albion the Shrouded Dragon")
            elif("Blazing Cartesia, the Virtuous" not in hand and "Blazing Cartesia, the Virtuous" in deck):
                hand.append("Blazing Cartesia, the Virtuous")
                deck = remove_card(deck,"Blazing Cartesia, the Virtuous")
            elif(check_card_count(hand,"Fallen of Albaz") != 3):
                hand.append("Fallen of Albaz")
                deck = remove_card(deck,"Fallen of Albaz")
            if(regained_activated):
                draw = generate_hands(deck,1,1)
                deck.append("Tri-Brigade Mercourier")
                for card in draw[0]:
                    hand.append(card)
                    deck = remove_card(deck,card)
        else:
            unoptimal_dark_monsters = [  "Fallen of Albaz", 
            "Edge Imp Chain",   "Dramaturge of Despia",    "Ad Libitum of Despia",    
            "Bystial Magnamhut",   "Bystial Saronir",  "Bystial Druiswurm",  "Albion the Shrouded Dragon"]

            for card in hand:
                if card in unoptimal_dark_monsters:
                    hand = remove_card(hand, card)
                    if(regained_activated):
                        draw = generate_hands(deck,1,1)
                        deck.append(card)
                        for card in draw[0]:
                            hand.append(card)
                            deck = remove_card(deck, card)
                    
                    break
        
        if(albion_activated == False and "Albion the Shrouded Dragon" in hand): #has to be done on resolution of regained draw
            if("Aluber The Jester of Despia" in hand and "Branded Opening" in deck):
                albion_activated = True
                deck = remove_card(deck, "Branded Opening")
                draw = generate_hands(deck,1,1)
                deck.append("Albion the Shrouded Dragon")
                hand = remove_card(hand,"Albion the Shrouded Dragon")
                for card in draw[0]:
                    hand.append(card)
                    deck = remove_card(deck,card)
            elif("Branded Retribution" not in hand and "Branded Retribution" in deck):
                albion_activated = True
                deck = remove_card(deck, "Branded Retribution")
                draw = generate_hands(deck,1,1)
                deck.append("Albion the Shrouded Dragon")
                hand = remove_card(hand,"Albion the Shrouded Dragon")
                for card in draw[0]:
                    hand.append(card)
                    deck = remove_card(deck,card)
            elif("Branded Opening" in deck):
                albion_activated = True
                deck = remove_card(deck, "Branded Opening")
                draw = generate_hands(deck,1,1)
                deck.append("Albion the Shrouded Dragon")
                hand = remove_card(hand,"Albion the Shrouded Dragon")
                for card in draw[0]:
                    hand.append(card)
                    deck = remove_card(deck,card)
            elif("Fallen of Albaz" in deck):
                albion_activated = True
                deck = remove_card(deck, "Fallen of Albaz")
                draw = generate_hands(deck,1,1)
                deck.append("Albion the Shrouded Dragon")
                hand = remove_card(hand,"Albion the Shrouded Dragon")
                for card in draw[0]:
                    hand.append(card)
                    deck = remove_card(deck,card)
    
    return hand



def dark_check(hand):
    dark_monsters = [  "Fallen of Albaz", 
            "Edge Imp Chain",   "Dramaturge of Despia",    "Ad Libitum of Despia",   "Tri-Brigade Mercourier", 
            "Bystial Magnamhut",   "Bystial Saronir",  "Bystial Druiswurm",  "Albion the Shrouded Dragon"]  #these are dark monsters that don't directly help access branded fusion

    for card in hand:
        if card in dark_monsters:
            return True

    return False

def main_BF_checker(hand,deck):
    total_trag_count_in_deck =  check_card_count(deck,"Despian Tragedy")
    if "Branded Fusion" in hand:
        return True
    elif "Aluber The Jester of Despia" in hand:
        return True
    elif "Branded Opening" in hand:
        return True
    elif "Foolish Burial" in hand and (check_card_count(hand,"Despian Tragedy") != total_trag_count_in_deck):
        return True
    elif "Gold Sarcophagus" in hand and (check_card_count(hand,"Despian Tragedy") != total_trag_count_in_deck):
        return True
    elif "Allure of Darkness" in hand and "Despian Tragedy" in hand:
        return True
    elif "Frightfur Patchwork" in hand and "Despian Tragedy" in hand:
        if((check_card_count(hand,"Edge Imp Chain") != 2) and (check_card_count(hand,"Polymerization") != 2)):
            return True
    elif "Polymerization" in hand and "Despian Tragedy" in hand:
        copy_hand = hand
        copy_hand = remove_card(copy_hand, "Despian Tragedy")
        copy_hand = remove_card(copy_hand, "Polymerization")
        if(light_dark_check(copy_hand)):
            return True
    elif "Despia, Theater of the Branded" in hand and "Despian Tragedy" in hand:
        copy_hand = hand
        copy_hand = remove_card(copy_hand, "Despian Tragedy")
        copy_hand = remove_card(copy_hand, "Despia, Theater of the Branded")
        if(light_dark_check(copy_hand)):
            return True
    elif "Albion the Shrouded Dragon" in hand and "Despian Tragedy" in hand and "Branded in Red" in hand:
        return True
    elif "Branded in White" in hand and "Despian Tragedy" in hand:
        copy_hand = hand
        copy_hand = remove_card(copy_hand, "Despian Tragedy")
        copy_hand = remove_card(copy_hand, "Branded in White")
        if(light_dark_check(copy_hand)):
            return True
    else:
        return False

def access_to_branded_fusion(hands, deck):
    count = 0
    for hand in hands:
        if (main_BF_checker(hand,deck)):
            count +=1
        elif "Allure of Darkness" in hand:
            if(dark_check): # we want to see if there is a dark monster already in hand, otherwise it is too risky using allure
                hand = allure_adjust(hand, deck)
                if main_BF_checker(hand, deck):
                    count +=1
            
    return count

def count_bystials(hands):
    bystials = ["Bystial Magnamhut","Bystial Saronir","Bystial Druiswurm"]
    count= 0
    one= 0
    two = 0
    three = 0
    for hand in hands:
        for card in hand:
            if card in bystials:
                count+=1
        
        if(count ==1):
            one+=1
        elif(count == 2):
            two+=1
        elif(count >= 3):
            three+=1
        
        count = 0

    return one, two, three

def check_clogginess(hands):
    aluber = ["Aluber The Jester of Despia","Foolish Burial", "Gold Sarcophagus","Branded Opening"]
    clogged = 0
    for hand in hands:
        count = 0
        for card in hand:
            if card in aluber:
                count+=1
        
        if (count > 1):
            clogged += 1
    
    return(clogged)


def deck_simulation_analysis(deck):
    print(count_cards(deck))
    hand_size = 5
    num_iterations = 100000
    sample_hands = generate_hands(deck, num_iterations, hand_size)
    #sample_hands = [['Allure of Darkness', 'Branded Regained', 'Fallen of Albaz', 'Tri-Brigade Mercourier', 'Branded in Red']]
    #print(sample_hands)
    total_hands_with_BF = access_to_branded_fusion(sample_hands, deck)
    one_bystial, two_bystial, three_bystial = count_bystials(sample_hands)
    print("There was ", total_hands_with_BF, " hands that had access to Branded Fusion.")
    print("Access to Branded Fusion to Total Hands  % = ", total_hands_with_BF / len(sample_hands) * 100)
    print("Hands with 1 Bystial: ", one_bystial, ", Hands with 2 Bystials: ", two_bystial, ", Hands with 3 Bystials: ", three_bystial)
    print("% 1 Bystial: ", one_bystial/len(sample_hands) * 100, ", % 2 Bystials: ", two_bystial/len(sample_hands) * 100, ", % 3 or more Bystials: ", three_bystial/len(sample_hands) * 100)
    print("This is how many times the deck clogged on Aluber: ", check_clogginess(sample_hands)/len(sample_hands) * 100, "%")

def main():
    # This is the 48 card decklist with allure
    deck_48 = [   
    "Aluber The Jester of Despia", "Aluber The Jester of Despia", "Aluber The Jester of Despia",    
    "Fallen of Albaz",    "Fallen of Albaz",    "Fallen of Albaz",    
    "Despian Tragedy",    "Despian Tragedy",    "Despian Tragedy",     
    "Edge Imp Chain",    "Edge Imp Chain",    "Dramaturge of Despia",    "Ad Libitum of Despia",    
    "The Bystial Lubellion",    "The Bystial Lubellion",    "Bystial Magnamhut",    "Bystial Magnamhut",    
    "Bystial Magnamhut",    "Bystial Saronir",    "Bystial Saronir",    "Bystial Saronir",    
    "Bystial Druiswurm",    "Bystial Druiswurm",   "Tri-Brigade Mercourier",    "Albion the Shrouded Dragon",    
    "Blazing Cartesia, the Virtuous",    "Branded Fusion",    "Branded Fusion",    "Branded Fusion",
    "Branded Opening",    "Branded Opening",    "Branded Opening",    "Branded in Red",    "Branded Regained",    "Branded Lost",  
    "Despia, Theater of the Branded",    "Polymerization",    "Polymerization",    "Super Polymerization",    "Super Polymerization",    "Super Polymerization",    
    "Allure of Darkness",    "Allure of Darkness",   "Frightfur Patchwork",    "Frightfur Patchwork",    
    "Branded Beast",    "Branded Banishment",    "Branded Retribution"]
    
    deck_51 = [   
    "Aluber The Jester of Despia", "Aluber The Jester of Despia", "Aluber The Jester of Despia",    
    "Fallen of Albaz",    "Fallen of Albaz",    "Fallen of Albaz",    
    "Despian Tragedy",    "Despian Tragedy",    "Despian Tragedy",     
    "Edge Imp Chain",    "Edge Imp Chain",    "Dramaturge of Despia",    "Ad Libitum of Despia",    
    "The Bystial Lubellion",    "The Bystial Lubellion",    "Bystial Magnamhut",    "Bystial Magnamhut",    
    "Bystial Magnamhut",    "Bystial Saronir",    "Bystial Saronir",    "Bystial Saronir",    
    "Bystial Druiswurm",    "Bystial Druiswurm", "Bystial Druiswurm",   "Tri-Brigade Mercourier",    "Albion the Shrouded Dragon",    
    "Blazing Cartesia, the Virtuous",    "Branded Fusion",    "Branded Fusion",    "Branded Fusion", "Foolish Burial", "Gold Sarcophagus",
    "Branded Opening",    "Branded Opening",    "Branded Opening",    "Branded in Red",    "Branded Regained",    "Branded Lost",  
    "Despia, Theater of the Branded",    "Polymerization",    "Polymerization",    "Super Polymerization",    "Super Polymerization",    "Super Polymerization",    
    "Allure of Darkness",    "Allure of Darkness",   "Frightfur Patchwork",    "Frightfur Patchwork",    
    "Branded Beast",    "Branded Banishment",    "Branded Retribution"]
        
    deck_42_no_patchwork = [   
    "Aluber The Jester of Despia", "Aluber The Jester of Despia", "Aluber The Jester of Despia",    
    "Fallen of Albaz",    "Fallen of Albaz",    "Fallen of Albaz",    
    "Despian Tragedy",    "Despian Tragedy",    "Despian Tragedy",     
    "Dramaturge of Despia",    "Ad Libitum of Despia",    
    "The Bystial Lubellion",    "The Bystial Lubellion",    "Bystial Magnamhut",    "Bystial Magnamhut",    
    "Bystial Magnamhut",    "Bystial Saronir",    "Bystial Saronir",    "Bystial Saronir",    
    "Bystial Druiswurm",    "Bystial Druiswurm",    "Tri-Brigade Mercourier",    "Albion the Shrouded Dragon",    
    "Blazing Cartesia, the Virtuous",    "Branded Fusion",    "Branded Fusion",    "Branded Fusion",  
    "Branded Opening",    "Branded Opening",    "Branded Opening",    "Branded in Red",    "Branded Regained",    "Branded Lost",    
    "Despia, Theater of the Branded",    "Super Polymerization",    "Super Polymerization",    "Super Polymerization",    
    "Allure of Darkness",    "Allure of Darkness",    
    "Branded Beast",    "Branded Banishment",    "Branded Retribution"]
    
    optimized_deck_40 = [   
    "Aluber The Jester of Despia", "Aluber The Jester of Despia", "Aluber The Jester of Despia",    
    "Fallen of Albaz",    "Fallen of Albaz",    "Fallen of Albaz",    
    "Despian Tragedy",    "Despian Tragedy",    
    "Dramaturge of Despia",    
    "The Bystial Lubellion",    "The Bystial Lubellion",    "Bystial Magnamhut",    "Bystial Magnamhut",    
    "Bystial Magnamhut",    "Bystial Saronir",    "Bystial Saronir",    "Bystial Saronir",    
    "Bystial Druiswurm",    "Bystial Druiswurm",    "Tri-Brigade Mercourier",    "Albion the Shrouded Dragon",    
    "Blazing Cartesia, the Virtuous",    "Branded Fusion",    "Branded Fusion",    "Branded Fusion", "Foolish Burial", "Gold Sarcophagus",     
    "Branded Opening",    "Branded Opening",    "Branded Opening",    "Branded in Red",    "Branded Regained",    "Branded Lost", 
    "Despia, Theater of the Branded", "Super Polymerization",    "Super Polymerization",    "Super Polymerization", 
    "Branded Beast",    "Branded Banishment",    "Branded Retribution"]
    
    deck_45_no_patchwork_add_foolish_gold = [   
    "Aluber The Jester of Despia", "Aluber The Jester of Despia", "Aluber The Jester of Despia",    
    "Fallen of Albaz",    "Fallen of Albaz",    "Fallen of Albaz",    
    "Despian Tragedy",    "Despian Tragedy",    "Despian Tragedy",     
    "Dramaturge of Despia",    "Ad Libitum of Despia",    
    "The Bystial Lubellion",    "The Bystial Lubellion",    "Bystial Magnamhut",    "Bystial Magnamhut",    
    "Bystial Magnamhut",    "Bystial Saronir",    "Bystial Saronir",    "Bystial Saronir",    
    "Bystial Druiswurm",    "Bystial Druiswurm",  "Bystial Druiswurm",  "Tri-Brigade Mercourier",    "Albion the Shrouded Dragon",    
    "Blazing Cartesia, the Virtuous",    "Branded Fusion",    "Branded Fusion",    "Branded Fusion",  "Foolish Burial", "Gold Sarcophagus",
    "Branded Opening",    "Branded Opening",    "Branded Opening",    "Branded in Red",    "Branded Regained",    "Branded Lost",    
    "Despia, Theater of the Branded",    "Super Polymerization",    "Super Polymerization",    "Super Polymerization",    
    "Allure of Darkness",    "Allure of Darkness",    
    "Branded Beast",    "Branded Banishment",    "Branded Retribution"]

    deck_optimized_w_patchwork = [   
    "Aluber The Jester of Despia", "Aluber The Jester of Despia", "Aluber The Jester of Despia",    
    "Fallen of Albaz",    "Fallen of Albaz",    
    "Despian Tragedy",       
    "Ad Libitum of Despia",    
    "The Bystial Lubellion",    "The Bystial Lubellion",    "Bystial Magnamhut",    "Bystial Magnamhut",    
    "Bystial Magnamhut",    "Bystial Saronir",    "Bystial Saronir",    "Bystial Saronir",    
    "Bystial Druiswurm",    "Bystial Druiswurm",  "Tri-Brigade Mercourier",    "Albion the Shrouded Dragon",
    "Edge Imp Chain",    "Edge Imp Chain",   
    "Blazing Cartesia, the Virtuous",    "Branded Fusion",    "Branded Fusion",    "Branded Fusion",
    "Branded Opening",    "Branded Opening",    "Branded Opening",    "Branded in Red",    "Branded Regained",    "Branded Lost",    
    "Despia, Theater of the Branded",    "Super Polymerization",    "Super Polymerization",    "Foolish Burial",
    "Frightfur Patchwork",    "Frightfur Patchwork", "Polymerization",    "Polymerization",      
    "Branded Beast",    "Branded Banishment",    "Branded Retribution"]
    print("Let's test each variant")
    print("This is the the 48 count variant: ")
    deck_simulation_analysis(deck_48)
    print("This is the 51 card variant w/ foolish, gold sarc, and third druiswurm: ")
    deck_simulation_analysis(deck_51)
    print("This is the 42 card variant (48 cards minus patchwork engine): ")
    deck_simulation_analysis(deck_42_no_patchwork)
    print("This is the 40 card variant (removed 1 tragedy, 1 ad lib, 2 allure. Added foolish and gold sarc): ")
    deck_simulation_analysis(optimized_deck_40)
    print("This is the 45 card variant (51 cards minus patchwork engine): ")
    deck_simulation_analysis(deck_45_no_patchwork_add_foolish_gold)
    print("This is a more optimized build without foolish and gold sarc and 8 bystials. patchwork included: ")
    deck_simulation_analysis(deck_optimized_w_patchwork)
if __name__ == "__main__":
    main()