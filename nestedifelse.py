#nested if else
print("Welcome to the rollercoaster :")
height = int(input("Enter your height : "))
if height >= 120:
    print("You can ride the roller coaster :")
    age = int(input("Enter your age: "))
    if age <= 18:
        print("Please pay 7 dollars...")
    else:
        print("Please pay 12 dollars...")
else:
    print("you cannot ride the roller coaster.....")