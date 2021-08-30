import random

high_score = 0

def dice_game():
    global high_score
    while True:
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice:")
        if choice == "1":
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            print("You roll a...", roll1)
            print("You roll a...", roll2)
            total = roll1 + roll2
            print("You have rolled a total of:", total)
            if total > high_score:
                print("New High Score!")
                high_score = total

        elif choice == "2":
            print("Thanks for playing.")
            break
        else:
            print("Invalid choice")
dice_game()