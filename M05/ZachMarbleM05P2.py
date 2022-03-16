#Name: (Zachary Marble)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 02-24-22
#Project #: MO5_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import zmconverter as c # importing the converter program

# display intro message
print("Zach Marble's Feet / Meters Converter")
print()

# defining the welcome function 
def fm_welcome():
    print("Zach Marble's Feet and Meter's Calculator") # displays welcome message
    print()

# defining the conversion selection menu
def fm_menu(): 

    # displays the menu title, with conversion options
    print("Conversions Menu:") 
    print("a. Feet to Meters")
    print("b. Meters to Feet")

# main conversion function
def main():
    fm_welcome() # call in welcome function

    # while loop for running the main conversions
    while True:
        fm_menu() # call in menu function to display menu options.

        choice = input("Select A Conversion (a/b): ") # gather user input to choose which conversion they want
        print()

        # main if statement that takes the user input and uses it to choose and the perform a conversion
        if choice.lower() == 'a': # first if statement that acts if user selects option a 
            feet = float(input("Enter feet: ")) # gather user input for the value of feet
            c.to_meters(feet) # call the conversion function for feet to meters function

        elif choice.lower() == 'b': # second if condition that acts if user chooses option 'b'
            meters = float(input("Enter meters: ")) # gathering user input for meters value
            c.to_feet(meters) # call the meters to feet conversion function

        else: # final else condition that displays an error message if user unputs neither a or b for selection
            print("You did not enter a valid selection.") # display error message
        
        more = input("Would you like to perform another conversion? (y/n): ") # gather user input to perform another conversion or not
        print()

        if more.lower() != 'y': # if else statement to either continue with more conversions or end the program
            print("Goodbye!") # print end message
            break # end program
        else:
            True # keep while loop as true to continue with conversions.

if __name__ == "__main__": main() # if statement to call main function.