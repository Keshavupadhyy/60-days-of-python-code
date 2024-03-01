print("Welcome to the rollercoaster :")
height = int(input("Enter your height : "))
if height >= 120:
    print("You can ride the roller coaster :")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Please pay 5 dollars...")
    elif age <= 18:
        print("Please pay 7 dollars...")
    elif age <=22:
        print("please pay 20 dollars...")
    else:
        print("Please pay 12 dollars...")
else:
    print("you cannot ride the roller coaster.....")