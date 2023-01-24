def tip_calculator():
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill? $"))
    percent_tip = float(input("What percentage tip would you like to give? "))
    amount_of_people = int(input("How many people to split the bill? "))
    final_calc = round((total_bill / 100 * percent_tip + total_bill) / amount_of_people, 2)
    print(f"Each person should pay {final_calc}$")


tip_calculator()
