# !/usr/bin/env python3

# display name and app title
print("Zach Marble Student Registration App")
print()

# gather variable values from student input
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth_year =  input("Birth Year: ")
print()

# display welcome message
print(f"Welcome {first_name} {last_name}!")
print("Your registration is complete.")
print()

# create password by concatenating user firstname and birthyear, as gathered from the user.
tempPassword = (first_name + "*" + birth_year)

# display temp password
print(f"Your temporary password is {tempPassword}.")