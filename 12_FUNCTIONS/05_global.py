def sum(x,y):
    print("Hey I am adding")
    c = x+y
    global z #This is refer to the global variable and not create a local
    z = 0 # reassigning the global variable
    return c
z = 10
print(z)
print(sum (4,6))
print(z)


x = 10
y = "Hello"
