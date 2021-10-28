# Programmer: Stel Carahaly
# Date: 10.11.21
# Program: ATM Bank Transaction

"""
This Program simulates an ATM utilizing if elif and else statements
Nesting If statements and refresh our comparison and logical operators
"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account\n")

# Set up account by asking users for first and last names using Variables
firstName = input("What is your first name: ")
lastName = input("What is your last name: ")
print("\nWelcome to Cash-R-Us", firstName, lastName + ", we will now set up a security pin on your account. \n")
# set up a PIN - personal identification number
pin = input("Please choose a 4-digit Personal Identification Number: ")
print("\nThank you", firstName, lastName + ", your pin is set to", pin)

# confirming correct pin
ans = input("is that correct? Y for yes or N for No: ")
if ans == "y":
    print("your pin has been saved as", pin)
    # making the transaction
    userPin = input("\nplease enter your 4 digit security pin: ")
    if pin == userPin:
        print("Welcome", firstName, lastName, "\nwould you like to make a transaction through our Automated Teller "
                                              "Machine?")
        ansr = input("Y for Yes, N for No:").lower()
        balance = 100
        # withdrawal or deposit using if elif
        if ansr == "y":
            print("\n********************************************************************\n")
            print("\nyour balance is $" + str(balance))
            print("would you make a withdrawal or deposit?")
            transaction = input("\nW for Withdrawal D for deposit: ").lower()
            amount = int(input("enter an amount: $"))
            if transaction == "w":
                balance = balance - amount
            elif transaction == "d":
                balance = balance + amount
            # print new balance
            if balance < 0:
                print("you cannot have a negative balance")
            else:
                print("\n Your final balance is $" + str(balance))
    else:
        print("sorry, your pin doesn't match our records, please try again")

"""

    else:
        print("\nThank you for visiting Cash-R-Us ATM", firstName, lastName)
# WHY ISN'T IT NESTING HJFGJFKFHGF
else:
    print("please retype your pin")
"""