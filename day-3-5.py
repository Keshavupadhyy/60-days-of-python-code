#lovecalculator
print("Welcome to the love calculator")
name1 = input("Enter your name : ")
name2 = input("enter your crush name : ")
cominend_string = name1 + name2
lower_case_string = cominend_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

pyar = int(str(true) + str(love))

if pyar > 10 or pyar > 90:
    print(f"you love score is {pyar}")
elif 40 <= pyar <= 50:
    print(f"your socre is {pyar}, your alll together..")
else:
    print(f"your sxore is {pyar}")