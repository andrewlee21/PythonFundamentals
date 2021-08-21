def show_balance(balance):
    balance = "{:.2f}".format(balance)
    print(balance)

def deposit(balance):
    amount = float(input("Enter amount to deposit:"))
    return amount + balance
    
def withdraw(balance):
    while True:
        amount = float(input("Enter amount to withdraw:"))
        if  balance - amount > -1:
            break
        print("Balance cannot fall below zero")
    return balance - amount

def logout(name):
    print("Goodbye", name)
    
