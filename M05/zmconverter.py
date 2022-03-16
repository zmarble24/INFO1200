#Name: (Zach Marble)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 02-24-22
#Project #: MO5_P2_converter
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# defined function for converting feet to meters
def to_meters(feet): # defined function using the feet variable, as input by user in the main function
    meters = round((feet * 0.3048), 2) # calculation for meters using the foot variable
    print(meters, "Meters") # display resulting value of meters
    print()

# defined function for converting meters to feet
def to_feet(meters): # defined function using the meter variable, as input by user in the main function
    feet = round((meters / 0.3048), 2) # calculation for feet using the meters variable
    print(feet, "Feet") # display resulting value of feet
    print()
