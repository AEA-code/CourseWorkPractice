# A Program for SmartFit team

# Q1: Ask the user to enter their age
try:
    user_age = int(input("Please enter your age: "))

    if user_age <= 0:  # stop the program if age is less or equal zero
        print("Age must be greater than zero.")
        exit()

    elif user_age < 18:
        print("You are eligible for the Teen Fitness Program.")

    elif user_age <= 40:
        print("You are eligible for the Regular Fitness Program.")

    else:
        print("You are eligible for the Senior Wellness Program.")


    # Q2: Ask about medical conditions
    user_medical = input(
        "Do you have any medical conditions? (yes or no): "
    ).strip().lower() # convert the prompt to lowercase

    if user_medical in ["yes", "no"]:

        if user_age >= 40 and user_medical == "yes":
            print("Medical clearance required before joining.")

        elif user_age < 40 or user_medical == "no":
            print("You can proceed with registration.")

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


    # Q3: Ask the user to choose a membership
    print("Enter membership type: Basic or Premium.")
    user_choice = input().strip().lower()

    # Nested conditional for Basic membership
    if user_choice == "basic":

        user_answer = input(
            "Do you want personal training? (yes or no): "
        ).strip().lower()

        if user_answer == "yes":
            print("Basic plan with personal training: $45 per month.")

        elif user_answer == "no":
            print("Basic plan: $30 per month.")

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Premium membership
    elif user_choice == "premium":
        user_answer = "no"
        print("Premium plan: $60 per month.")

    else:
        print("Invalid membership type. Please enter 'Basic' or 'Premium'.")
        user_answer = "no"


    # Nested logical conditions
    if user_choice == "premium" and user_age < 30:
        print("You qualify for a youth discount! 10% off your plan.")

    if user_choice == "basic" and user_answer == "no":
        print("Consider upgrading to Premium for more benefits!")

    if user_medical == "yes" and user_choice == "premium":
        print("We recommend a free consultation before starting.")


except ValueError:
    print("Please enter a valid whole number for your age.")