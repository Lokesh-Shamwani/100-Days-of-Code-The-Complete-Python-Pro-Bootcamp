print("Welcome to the tip calculator.")
bill = input("what was the total bill? $")
perc_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
pplz = input("How many people to split the bill? ")

bill = float(bill)
increase = bill * float(int(perc_tip) / 100)
bill += increase

per_head_cost = bill / int(pplz)

print(f"Each person should pay: ${round(per_head_cost,2)}")
