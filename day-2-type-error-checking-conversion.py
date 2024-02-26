#len() function is not working with int()
#---------------------------------------------------------------------------------------------------------------------------------

# num_char = len(input("what is your name: "))
# print("your name has " + num_char + "characters.")
# what is your name: keshav
# Traceback (most recent call last):
#   File "C:\Users\keshav upadhyay\60 days of python code\type-error-checking-conversion.py", line 3, in <module>
#     print("your name has " + num_char + "characters.")
#           ~~~~~~~~~~~~~~~~~^~~~~~~~~~
# TypeError: can only concatenate str (not "int") to str

# ---------------------------------------------------------------------------------------------------------------------------------

#type checking

# num_char = len(input("what is your name: "))
# print(type(num_char))

# ---------------------------------------------------------------------------------------------------------------------------------

#type conversion

# num_char = len(input("what is your name: "))
# new_num_char = str(num_char)
# print("your name has " + new_num_char + "characters.")
#
# a =str(123)
# print(type(a))


# a =float(123)
# print(type(a))

# print(70 + float("100.5"))

# print(str(70) + str(100))