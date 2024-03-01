#leapyear
print("Welcome to the leap year calculator : ")
year = int(input("Which your to check: "))
if year % 4 == 0:
    print("leap year")
elif year % 100 == 1:
    print("no leap year")
elif year % 400 == 0:
    print("leap yeear")
else:
    print("not leap year")