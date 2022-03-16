#Name: (Zachary Marble)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 02-24-22
#Project #: MO5_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

# display program title
print("Zachary Marble's Even or Odd Checker")
print()

# defining function for is_even
def is_even(num): 
    if num % 2 == 0: # if there is no remainder when divided by 2
       print("This is an Even Number.") # if true, then displays message stating the number is even
    else:
        print("This number is odd.") # if false, then displays message stating the number is even

def main(): # defined main function
    print("Zach's Even or Odd Checker") # display welcome message
    print()

    my_num = float(input("Enter an Integer: ")) # gather user input for number value
    
    is_even(my_num) # calls is_even function

if __name__ == "__main__": main() # calls main function
