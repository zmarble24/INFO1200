#!/usr/bin/env python3

# display my name
print("Zach's Rectangle App")
print()

# display a welcome message
print("Welcome to The Rectangle Calculator")
print("====================================")

# Gather user measurments for width and length
width = float(input("Enter the measurement for width:  "))
length = float(input("Enter the measurement for length: "))
print()

# calculate area and perimeter
area = round(length * width, 2)
perimeter = round((2 * length) + (2 * width), 2)

            
# format and display the resulting calculations
print("=====================")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
print()
print("Bye")


