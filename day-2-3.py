#life in weeks exercise

age = input("Enter your age :  ")
age = int(age)
years_reaming = 90 - age
days_remaing = years_reaming * 365
week_remaingn = years_reaming * 52
month_remaing = years_reaming * 12

print(f"you have days {days_remaing} , weeks have {week_remaingn} , months have {month_remaing} left")
