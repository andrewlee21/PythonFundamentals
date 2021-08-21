from banking_pkg import account 

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
print("          === Automated Teller Machine ===          ")
while True: 
    user = input("Enter name to register: ")
    if len(user)<11:
        break
    print("Usernames must be less than 10 characters")
while True:
    pin = input("Enter PIN:")
    if len(pin)==4:
        break
    print("PIN must be 4 characters")
balance = 0
print(user, "has been registered with a starting balance of $", balance)

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name:")
    pin_to_validate = input("Enter PIN:")
    if name_to_validate == user and pin_to_validate == pin:
        print("Login Successful")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(user)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
    elif option == "3":
        balance = account.withdraw(balance)
    elif option == "4":
        account.logout(user)
        break

