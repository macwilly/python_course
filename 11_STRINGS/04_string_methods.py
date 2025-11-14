# string are immutability

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

lotsOfWhiteSpace = "      White  Space      "
print(lotsOfWhiteSpace)
print(lotsOfWhiteSpace.strip())
print(lotsOfWhiteSpace.lstrip())
print(lotsOfWhiteSpace.rstrip())