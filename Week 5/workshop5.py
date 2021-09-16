import random

def guess_random_number(tries, start, stop):
    target=random.randint(start,stop)
    while tries!=0:
        print(f"You have {tries} tries remaining.")
        guess = int(input(f"Guess a number between {start} and {stop}: "))
        if guess < stop and guess > start:
            if guess == target:
                print("Correct! :)")
                return
            elif guess > target:
                print("Guess was too high")
            elif guess < target:
                print("Guess was too low")
        else:
            print(f"Guess must be larger than {start} and less than {stop}")  
        tries -= 1

    print("Out of tries, Game Over :(")

def guess_random_num_linear(tries, start, stop):
    target = random.randint(start,stop)
    print(target)
    for x in range(start, stop,1):
        print(x)
        if x == target:
            print("Correct")
            return
        tries -=1
        print(f"You have {tries} tries remaining")
        if tries == 0:
            print("Game over :(")
            return

# guess_random_number(3,4,20)

guess_random_num_linear(5,4,20)

