#Name: (Zachary Marble)
#Class: (INFO 1200)
#Section: (01)
#Professor: (Crandall)
#Date: Feb. 02, 2022
#Project #: 1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

#define and print my full name
firstName = "Zachary Marble"  
print("Hello, my name is " + firstName)

#define and display my school                       
school= 'Utah Valley University'
print('I go to' + ' ' + school)

# define values for credits and classes variables, then using those variables for the totalcredits variable, which calculates the total credits taken this semester
credits = 3
classes = 6
totalcredits = credits * classes

print('If I take 6 classes this semester and all are three credits each, I will be taking ' + str(totalcredits) + ' credits')

print('I would like to save money by taking this many credits.')

maxCredits = 12
costPerClass = 350
classFee = 20

totalCostPerSemester = round(((totalcredits - maxCredits) / credits) * ( costPerClass + classFee), 2)

print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.')

totalCostPerYear = round((totalCostPerSemester), 2) * 3

print('That is a wopping $' + str(totalCostPerYear) + ' a year!')

print('This was a very informative and worth while Python assignment!')
