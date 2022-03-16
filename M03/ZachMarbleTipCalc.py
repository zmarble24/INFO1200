# !/usr/bin/env python3

# display name and program title
print("Zach Marble Tip Calculator")
print()

# gather user input for meal cost and tip percentage
costOfMeal = float(input("Cost of Meal: "))
tipPercentage = float(input("Tip Percentage: "))
print()

tipAmount = round(costOfMeal * (tipPercentage / 100), 2) # use user input to calculate tip amount
print(f"Tip Amount: ${tipAmount}.") # display tip amount

totalAmount = tipAmount + costOfMeal # Calculate total amount using the calculated tipamount and meal cost
print(f"Total Cost: ${totalAmount}.") # display total amount 
