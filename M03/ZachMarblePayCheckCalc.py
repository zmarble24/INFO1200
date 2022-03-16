# !/usr/bin/env python3

# display name and app title
print("Zachary  Marble Pay Check Calculator")
print()

# gather user input for user's hours worked and hourly rate
hoursWorked = float(input("Hours Worked: "))
payRate = float(input("Hourly Rate: "))
print()

# calculate total pay based on hours times rate
grossPay = round(hoursWorked * payRate, 2)
print(f"Gross pay: {grossPay}")

# add in tax rate and use to calculate tax amount and then display rate and amount.
taxRate = 18
print(f"TaxRate: {taxRate}%")
taxAmount = grossPay * (taxRate / 100)
print(f"Tax Amount: {taxAmount}")

# use tax amount to calculate take home pay, then display
takeHomePay = round(grossPay - taxAmount, 2)
print(f"Take Home Pay: {takeHomePay}")

