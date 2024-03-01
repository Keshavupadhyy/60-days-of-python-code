print("Welcome to the rollercoaster :")
height = int(input("Enter your height : "))
bill = 0
if height >= 120:
    print("You can ride the roller coaster :")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Please pay 5 dollars...")
    elif age <= 18:
        bill = 7
        print("Please pay 7 dollars...")
    elif  age >45 and age < 55:
        print("ride is free")
    else:
        bill = 12
        print("Please pay 12 dollars...")
    wants_photo = input("do you taken photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"your final bill is {bill}")

else:
    print("you cannot ride the roller coaster.....")