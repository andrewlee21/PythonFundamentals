import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    menu = input("Press 'Enter' to pick a card, or 'Q' to quit")
    if menu.lower == "q":
        break
    pick = diamonds[random.randint(0,len(diamonds)-1)]
    diamonds.remove(pick)
    hand.append(pick)
    print("Remaining cards:", diamonds)
    print("Your hand:", hand)
       
if not diamonds:
    print("There are no more cards to pick")