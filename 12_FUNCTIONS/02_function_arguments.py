def add(a,b):
    return a+b

c = add(1,2)
print(c)

# Default arguments

def greeting(name = "Steve"):
    return f"Hello {name}!"

print(greeting())
print(greeting("Jack"))

# Keyword arguments. Allow the developer to put the arguments in any order as long as the name is used.

d = add(b=6,a=10)
print(d)
