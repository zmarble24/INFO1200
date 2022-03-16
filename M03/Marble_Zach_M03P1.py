#!/usr/bin/env python3

#print app name
print("Zach Marble's MPG App")
print()

# display a welcome message
print("Welcome to The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t\t"))
cost = float(input("Enter the Cost of Gas per Gallon:\t"))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)
total_cost = round(gallons_used * cost, 2)
mileage_cost = round(cost / mpg, 2)
            
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total Cost for Gas:\t\t{total_cost}")
print(f"Cost per Mile:\t\t\t{mileage_cost}")
print()
print("Bye")