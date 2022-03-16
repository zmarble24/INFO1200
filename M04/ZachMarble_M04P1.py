#Name: (Zachary Marble)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: MO4_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Zach Marble Letter Grade Converter") # displays name and program title
print()

choice = 'y' # setting choice variable to 'y' to start the following while loop
while choice.lower() == 'y': # beginning of while loop
    
    number = int(input('Enter the Numerical Grade: ')) # gather user input for numerical grade
    
    if number >= 94 : # if loop where each step creates a value for the letter grade based on the number input by user.
        letter = 'A'
    elif number < 94 and number >= 90 :
        letter = 'A-'
    elif number < 90 and number >= 87 :
        letter = 'B+'
    elif number < 87 and number >= 83 :
        letter = 'B'
    elif number < 83 and number >= 80 :
        letter = 'B-'
    elif number < 80 and number >= 77 :
        letter = 'C+'
    elif number < 77 and number >= 73 :
        letter = 'C'
    elif number < 73 and number >= 70 :
        letter = 'C-'
    elif number < 70 and number >= 67 :
        letter = 'D+'
    elif number < 67 and number >= 63 :
        letter = 'D'
    elif number < 63 and number >= 60 :
        letter = 'D-'
    else :
        letter = 'E'
    
    print(f'Letter Grade: {letter}') # display letter value
    print()
    
    choice = input('Continue? (y/n): ') # Gather user input to either restart the while loop and convert more grades, or end the program.
    print()

print('Bye!') # display end message

