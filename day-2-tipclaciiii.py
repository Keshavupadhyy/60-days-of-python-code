print("Welcome to the tip claculator")
Bill = float(input("What was the total bill? "))
tip = int(input("how much tip do you like to give? 10,12 or 15? "))
people = int(input("how many people to split  the bill: "))

bil_with_tip = tip / 100 * Bill + Bill
print(bil_with_tip)
