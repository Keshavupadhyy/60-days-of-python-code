#BMI clacii...

height = input("enter your height in m : ")
weight = input("enter your weight in kg : ")

body_mass = int(weight) / float(height) ** 2

bmi = int(body_mass)
print(bmi)