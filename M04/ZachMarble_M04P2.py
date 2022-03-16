#Name: (Zachary Marble)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# display program name
print("Zach Marble's Tip Calculator")
print()

# Gather User Input for Meal Cost Variable
meal_cost = float(input("Cost of Meal: "))
print()

tip_percent = [15, 30, 5] # Set Percentage Amounts
for i in tip_percent: # for loop that calculates tip and total amount using the meal cost input and preset percentages
    print(f"{i}%")
    tip_amount = round(meal_cost * (i / 100), 2)
    print(f"Tip Amount: {tip_amount}")
    meal_total = tip_amount + meal_cost
    print(f"Total Amount: {meal_total}")
    print()

print("Bye!") # Ending Message