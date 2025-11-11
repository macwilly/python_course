# Strings are full objects that you can auto index
name = "Mackenzie"
print(name[0])
print(name[-1])
print(name.__len__())
print(name[name.__len__()-1])


# Index of will get the first instance of a character in a string
char = 'e'
if char in name:
    print(name.index(char))
else:
    print(f"'{char}' not found in '{name}'")