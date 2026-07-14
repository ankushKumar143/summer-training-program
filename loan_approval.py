# Loan Approval Program
while True:
    print("=" * 50)
    print("Loan Approval Program")
    print("=" * 50)
    name = input("Enter your name: ")

    # age validation
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue

    if age < 0 and age > 120:
        print("Invalid age. Please enter a valid age.")
        continue

    # salary validation
    try:
        salary = float(input("Enter your salary: "))
    except ValueError:
        print("Invalid input. Please enter a valid salary.")
        continue

    if salary < 0:
        print("Invalid salary. Please enter a valid salary.")
        continue

    # loan amount validation
    try:
        loan_amount = float(input("Enter the loan amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid loan amount.")
        continue

    if loan_amount < 0:
        print("Invalid loan amount. Please enter a valid loan amount.")
        continue

    employment = input("Employment Status (Employed/Unemployed): ").lower()
    existing_loan = input("Do you already have a loan? (yes/no): ").lower()

    try:
        credit_score = int(input("Enter your credit score: "))
    except ValueError:
        print("Invalid credit score.")
        continue

    # loan approval
    if age >= 18 and age <=59:
        if employment == "employed":
            if existing_loan == "no":
                if salary >= 25000:
                    if credit_score >= 750:
                        interest = 8
                    elif credit_score >= 700:
                        interest = 10
                    elif credit_score >= 650:
                        interest = 12
                    else:
                        print("Loan not approved due to low credit score.")
                        continue

                    # EMI calculation
                    years = 5
                    emi = (loan_amount * interest * (1 + interest) ** years) / ((1 + interest) ** years - 1)
                    print(f"Loan approved. \n\nYour EMI is: {emi}")

                    print("\n================Loan Approved================")
                    print("Applicant :", name)
                    print("Loan Amount : ₹", loan_amount)
                    print("Interest Rate :", interest, "%")
                    print("Loan Duration :", years, "Years")
                    print("Monthly EMI : ₹", round(emi, 2))

                else:
                    print("\nLoan Rejected!")
                    print("Reason: Salary must be at least ₹25,000.")
                    continue
            else:
                print("\nLoan Rejected!")
                print("Reason: You already have a loan.")
                continue
        else:
            print("\nLoan Rejected!")
            print("Reason: You must be employed.")
            continue
    else:
        print("\nLoan Rejected!")
        print("Reason: You must be between 18 and 59 years old.")
        continue

    choice = input("Do you want to continue? (y/n): ").lower()
    if choice != "y":
        break





