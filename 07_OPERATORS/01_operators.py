# Most of the operators are what you would expect. There is floor division // which will return an int value
# Division will return a float even when it is a whole number.
print(10/3)
print(10//3)


# Conditional Operator
# These will always return a true or false value

string_a = "Hello"
string_b = "World"
if string_a == string_b:
    print("String is equal to string")
else:
    print("String is not equal to string")

# Logical Operator
# Logical operators are the words, not && ||
# Help us operate on two booleans
# NOT will negate the operator
c = True
d = False
print(c and d)
print(c or d)
print(not c)
