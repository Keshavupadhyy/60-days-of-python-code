#pizza order program
print("Welcome to the Pizza wala : ")
size = (input("What size of pizza you love? S, M, or L  "))
add_pepperoni = input("do you want pepeproni> Y or N ")
extra_cheese = input("do you want extra cheeze? y or N")
bill = 0

if size == "S":
    bill = 15
    print("pay 15 dollars..")
    if add_pepperoni == "Y":
        bill += 2
        print(f"ypu bill is {bill}")



elif size == "M":
    bill = 20
    print("pay 20 dollars..")
    if add_pepperoni == "Y":
      bill += 3
      print(f"ypu bill is {bill}")

elif size == "L":
    bill = 25
    print("pay 25 dollars..")
    if add_pepperoni == "Y":
        bill += 3
        print(f"ypu bill is {bill}")
        
if extra_cheese == "Y":
    bill += 1


print(f"total bill is {bill}")