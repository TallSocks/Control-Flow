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
print("\nWelcome to Cash-R-Us", firstName,lastName + ", we will now set up a security pin on your account. \n")
# set up a PIN - personal identification number
pin = input("Please choose a 4-digit Personal Identification Number: ")
print("\nThank you", firstName, lastName + ", your pin is set to", pin)
"""
# IDEA FOR LATER
# confirming correct pin
ans = input("is that correct? Y for yes or N for No: ")
if ans == "y"
    print("your pin has been saved as", pin)
elif ans == "n"
    print("please retype your pin")
"""
print("\nWould you like to make a transaction through our Automated Teller Machine:")
"""
print input("\nY for Yes \nN for No")
"""