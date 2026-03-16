print("Welcome to the tip calculator!")
bill  = float(input("What was the total bill? $"))
tip_p = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

bill_w_tip = bill + (bill*(tip_p / 100))

bill_pp = bill_w_tip / total_people

print(f"Each person should pay: ${round(bill_pp, 2)}")