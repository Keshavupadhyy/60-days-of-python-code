#formated string
name = 'keshav'
age = 22
print(f"hello {name} you are {age} years old ") # this is highly recommended
print("hello {} you are {} years old " .format('keshav' , '22'))#this is new feature
print("hello {} you are {} years old " .format(name , age))#direcy access variable
print("hello {1} you are {0} years old " .format(name , age))#use numbers to swap the position
print("hello {new_name} you are {age} years old " .format(new_name='vichar', age=23))# create a new variable and put
# the on AA