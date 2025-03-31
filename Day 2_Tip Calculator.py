print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
total = (bill * ((tip/100)+1))/people
pay = "{:.2f}".format(total)
print(f"Each person should pay: ${pay}")