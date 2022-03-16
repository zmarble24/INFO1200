# Zach Marble Validation File for the Future Value App

# defined function to get and validate user input float values
def get_float(prompt,low,high): 

    while True: # Start while loop to test number unput
        number = float(input(prompt))# set number variable

        if number > low and number < high: # if statement that checks the input and responds accordingly
            return number
        else: print("Entry must be greater than", low, "and less than or equal to", high)

# defined function to get and validate user input integer values
def get_int(prompt, low, high):
    
    while True: # Start while loop to test number unput
        number = int(input(prompt)) # set number variable

        if number > low and number < high: # if statement that checks the input and responds accordingly
            return number
        else: print("Entry must be greater than", low, "and less than or equal to", high)

# defined main function
def main(): 

    choice = 'y' # set choice variable to start while loop
    while choice.lower() == 'y': # start of while loop
        valid_number = get_float("Enter Number:",0,1000) # get user input between 0 and 1000
        print("Valid Number =", valid_number) # display the valid number
        print()

        valid_integer = get_int("Enter Integer:",0,50) # get user input for user input int value
        print("Valid Integer =", valid_integer) # display valid int as input by the user
        print()
        
        choice = input("Repeat? (y/n):") # provide user with option to repeat or end
    
    print("Bye!") # display departure message

if __name__ == "__main__": # define if statement to begin validation program
    main()