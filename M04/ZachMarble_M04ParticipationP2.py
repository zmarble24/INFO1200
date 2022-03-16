#!/usr/bin/env python3

# display a welcome message
print("Welcome to Zach Marble's Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # while loop to validate user input for monthly investment variable
    is_valid = False
    while is_valid == False :

    # get input from the user for monthly investment
        monthly_investment = float(input("Enter monthly investment:\t"))
        
        # if loop to check what the user has set as the variable for monthly investment
        if monthly_investment > 0 and monthly_investment <= 1000 :
            is_valid = True
        else:
            print("Entry must be greater than 0 and less than 1000. Please try again.")

    is_valid = False # reset variable to start next while loop
    while is_valid == False : # start while loop 
        yearly_interest_rate = float(input("Enter yearly interest rate:\t")) # gather user input for variable yearly interest rate
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15 : # create if statement to check input for variable value.
            is_valid = True
        else :
            print("Entry must be greater than 0 and less than 15. Please try again.")

    is_valid = False # reset is_valid variable for next while loop
    while is_valid == False : # start while loop
        years = int(input("Enter number of years:\t\t")) # gather user input for term lenght in years
        if years > 0 and years <= 50 : # if loop to check the user assigned value for year term length
            is_valid = True
        else :
            print("Entry must be greater than 0 and less than 50. Please try again.")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
