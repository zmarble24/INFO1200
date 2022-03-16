def main():
    min_salary = 60000
    min_years = 5

    choice = "y"
    while choice.lower() == "y":
        salary = float(input("Enter Salary: "))
        years = int(input("Enter Years Worked: "))

        #if salary != float() and years != int():
            #print("Invalid input")
        

        if salary < min_salary:
            print("You must have a salary of more then $40,000")
        if years < min_years:
            print("You must have worked at least 3 years")
        if salary >= min_salary and years >= min_years:
            print("Qualified")
            
        choice = input("Try again? (y/n): ")
    print()

if __name__ == "__main__":
    main()
