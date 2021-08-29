def show_homepage():
    print("        === DonateMe Homepage ===         ")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register       |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations |")
    print("------------------------------------------")
    print("|              5.    Exit                |")
    print("------------------------------------------")
    
def donate(username):
    donation_amt = float(input("Enter amount to donate:"))
    donation = f"{username} donatated ${donation_amt}"
    print(f"Thank you, {username}. A donation has been made in the amount of ${donation_amt}")
    return donation

def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations")
    else:
        for d in donations:
            print(d)
