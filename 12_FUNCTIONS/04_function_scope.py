z = 8

def sum (a,b):
    c = a + b
    z = 1 # this is in local scope and not overwriting the other z. It is not recommend to do this
    return c

print(sum (4,6))


# You can only access local variables inside the function. Like a and b
# z is a 'global' variable because it is outside the local scope
