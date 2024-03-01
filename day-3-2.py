#BMI Calci... 2.0

print("welcome to the upgrade bmi calcultor:  ")
height = float(input("enter your height:  "))
weight = float(input("enter your weight: "))

body_mass = float(weight) / float(height) ** 2
print(body_mass)

if body_mass <= 18.5:
    print("your underweight....")
elif body_mass  <= 25:
    print("normal weight.....")
elif body_mass  <= 30:
    print("over weight....")
elif body_mass  <= 35:
    print("obses.....")
else:
    print("clinically obses")