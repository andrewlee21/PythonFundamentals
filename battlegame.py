
#Task 1
wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_dmg = 150
elf_dmg = 100
human_dmg = 20
dragon_dmg = 50

#Task 3
while True: 
    print("1) ", wizard)
    print("2) ", elf)
    print("3) ", human)
    character = input("Choose your character:")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_dmg = wizard_dmg
        break
    if character == "2":
        character = elf
        my_hp = elf_hp
        my_dmg = elf_dmg
        break
    if character == "3":
        character = human
        my_hp = human_hp
        my_dmg = human_dmg
        break
print("You have chosen the character:",character)
print("Health:", my_hp)
print("Damage:",my_dmg)


while True: 
    dragon_hp -= my_dmg
    print("The", character, "damaged the Dragon -", my_dmg, "points!" )
    print("The dragon's health is down to", dragon_hp)
    if dragon_hp <=0:
        print("The Dragon has lost the battle")
        break
    my_hp -= dragon_dmg
    print("The dragon damaged the", character, dragon_dmg, "points!" )
    print("The",character, "health is down to", my_hp)
    if my_hp <=0:
        print("The",character," has lost the battle")
        break