def login(database, username, password):
    if username.lower() in database and database[username.lower()]["pass"] == password:
         print("Welcome", username)
        # username = database[username]["reg_name"] 
         return username.lower()
    elif username.lower() in database and database[username.lower()] != password:
        print("Incorrect Pasword")
        return ""
    else:
        print("Username not in database, please try again.")   

def register(database, username):

    if username.lower() in database:
        print("\nUsername already exists.\n")
        return ""
    elif len(username)<11:
        print("\nThank you. Username", username,"has been registered. \n")
        return username
    else:
        print("Username must be greater than 10 characters")

        
