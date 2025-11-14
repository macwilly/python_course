# string are immutability
from operator import contains

name = "mackenzie"
print(name)
print(name.title())
#name[0] = "m" # Cannot do this
print(name)
# This is actually reassigning the value of name and not changing the string
name = "Willard"
print(name)

a = len(name)
print(a)

# Strip will remove the white space at the end/start/both of string

lots_of_white_space = "      White  Space      "
print(lots_of_white_space)
print(lots_of_white_space.strip())
print(lots_of_white_space.lstrip())
print(lots_of_white_space.rstrip())

# the find function will give the index of a character or group of characters

text = "python is fun"

print(text.find("is"))

# replace
print(text.replace("is", "was"))
fruit_string = "Pear,Orange,Kiwi"
print(fruit_string.split(","))

fruit_list = ["apple", "banana", "cherry"]
print(", ".join(fruit_list))

print(contains(text,"python"))
test_string =  "Python123"

print(test_string.isalpha())
print(test_string.isnumeric())
print(test_string.isdigit())
print(test_string.isalnum())
print(test_string.isspace())