#!/usr/bin/env python3

# display a welcome message
print("Zach Marble's Miles Per Gallon application")
print()

# create while loop to offer users the option to make more calculations
another_trip = 'y'
while another_trip.lower() == 'y':

# get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:  "))
    print()

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per Gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        total_gas_cost = round((gallons_used * cost_per_gallon), 2)
        cost_per_mile = round((total_gas_cost / miles_driven), 2)
        print(f"Miles Per Gallon: {mpg}")
        print(f"Total Cost of Gas: {total_gas_cost}")
        print(f"Cost per Mile: {cost_per_mile}")
        print()

        # gather user input to continue or cancel out of while loop
        another_trip = input("Get Entries for Another Trip? (y/n):  ")



print()
print("Bye")
