from donations_pkg import homepage
from donations_pkg import user

database = {"andrew": {"pass": "12345", "reg_name":"ANDREW"}, "andrew1":"12345"}
donations = []
authorized_user = ""
db_key = ""

while True:
    homepage.show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)
    choice = input("Choose an option:")
    if choice == "1" or choice == "2":
        username = input("Username:")
        while True:
            password = input("Password:")
            if len(password)<5:
                print("Password must be greater than 4 characters") 
            else:
                break
    if choice == "1":        
        authorized_user = user.login(database, username, password)
        db_key = username.lower()

    elif choice == "2":
        authorized_user = user.register(database, username)
        if authorized_user != "":
            database[authorized_user.lower()] = {"pass":password, "reg_name":authorized_user}
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else: 
            donation = homepage.donate(authorized_user)
            donation = "{:.2f}".format(donation)
            donations.append(donation)
    elif choice == "4":
        homepage.show_donations(donations)
    elif choice == "5":
        print("You are leaving the program. Goodbye <3")
        break
    else:
        print("Invalid input, please try again.")   
