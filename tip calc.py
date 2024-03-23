print("Welcome to the tip calculator")
a  = float(input("What was the total bill? $"))
b  = int(input("How much tip would you like to give? 10, 12, or 15?"))
c = int(input("How many people split the bill?"))

total = round((a/c)*((b/100)+1), 2)
print(f"Each person should pay {total}")