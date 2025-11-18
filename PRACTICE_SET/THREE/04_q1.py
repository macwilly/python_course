#Using format(), create a sentence "My name is John and I am 25 years old." Passing John and 25 as variables.
name = "John"
age = 25
string = "My name is {} and I am {} years old".format(name, age)
print(string)
# Do the same with f string
print(f"My name is {name} and I am {age} years old")