age =input("Are you a cigarette addict older than 75 year old? Please enter Yes or No: ").title()

chronic = input("Do you have a severe chronic disease? Please enter Yes or No: ").title()


immune = input("Is your immune system too weak? Please enter Yes or No: ").title()


risk = age and chronic and immune

if risk == "Yes":
    print("You are in risky group")
else:
    print("You are not in risky group")
