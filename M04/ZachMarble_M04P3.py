#Name: (Zachary Marble)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO4_P3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# display program name
print("Zach Marble's Change App")
print()

# set choice variable to y to begin while loop
choice = 'y'

# begin while loop
while choice.lower() == 'y':

    # Gather user input for value of cents
    cents = int(input("Enter the Number of Cents (0-99): "))
    print()

    quarters = cents // 25 # calculate number of Quarters
    cents = cents % 25

    dimes = cents // 10 # calculate number of dimes
    cents = cents % 10

    nickels = cents // 5 # calculate number of nickels
    cents = cents % 5

    pennies = cents // 1 # calculate number of pennies
    cents = cents % 1

    # display the calculated values for each type of coin
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")
    print()

    # display choice for user to continue or end the program
    choice =  input("Continue (y/n): ")
    print()

# display End message
print("Bye!")