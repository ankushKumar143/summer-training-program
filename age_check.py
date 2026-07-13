# Age Check for Driving License
while True:
    print("=" * 50)
    print("Age Check for Driving License")
    print("=" * 50)
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue

    if age < 0 and age > 120:
        print("Invalid age. Please enter a valid age.")
        continue

    if age < 18:
        print(f"\n{name}, you are not eligible for driving license.")
        print(f"You have to wait {18-age} year(s) to get your driving license.")

    elif age >= 18 and age <= 59:
        print(f"\nHello {name}!!")
        print(f"You are eligible for driving license.")

        vehicle = input("What vehicle you have: ").lower()
        if vehicle == "car":
            print("You can apply for a car driving license.")
        elif vehicle == "bike":
            print("You can apply for a bike driving license.")
        else:
            print("Unknown vehicle.")
        print("\nDriving Tips:")
        print("- Always wear a helmet (bike).")
        print("- Always wear a seat belt (car).")
        print("- Follow traffic rules.")
        print("- Never drink and drive.")
        print("- Do not use a mobile phone while driving.")

        print("\nReminder:")
        print("Being 18+ does NOT mean you can drive legally.")
        print("You must have a valid driving license.")

    else:
        print(f"Hello {name}!!")
        print(f"You are eligible for driving license.")
        print("You can apply for a car driving license.")
        print("\nDriving Tips:")
        print("- Always wear a helmet (bike).")
        print("- Always wear a seat belt (car).")
        print("- Follow traffic rules.")
        print("- Never drink and drive.")
        print("- Do not use a mobile phone while driving.")

        print("\nReminder:")
        print("Being 18+ does NOT mean you can drive legally.")
        print("You must have a valid driving license.")

    choice = input("Do you want to continue? (y/n): ").lower()
    if choice != "y":
        break

