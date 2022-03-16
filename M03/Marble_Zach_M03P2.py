#!/usr/bin/env python3

# display my name
print("Zach Marble's Test Score App")
print()

# display a welcome message
print("Welcome to The Test Scores Calculator")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
score1 = int(input("Enter 1st test score: "))
score2 = int(input("Enter 2nd test score: "))
score3 = int(input("Enter 3rd test score: "))
total_score = (score1 + score2 + score3)

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
print(f"Scores: {score1} {score2} {score3}")
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")


