import random
names_string = input("Give me everybody names by saturated comma:: ")
name = names_string.split(", ")
print(name)
random_name  = random.randint(0, 3)
if random_name == 0:
    print("keshav pay the bill")
elif random_name == 1:
    print("anegla pay the bill")
elif random_name == 2:
    print("ben pay the bill")
else:
    print("jenny pay the bill")