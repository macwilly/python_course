# Decorators will be used when writing APIs in flash or django
# decorator is a function that takes a functions, then in creates a new function and then will return the new function
def decorator(func):
    def wrapper():
        print('I will print hello')
        func()
        print("I printed")
    return wrapper


def say_hello():
    print("Hello World!")

say_hello()

# since decorator returns a function it needs to be assigned to a variable. also Note that you are passing the
# function as a variable so you do not add the ()
f = decorator(say_hello)
f()



########## Alt syntax for decorator add the @{functionName}


def dec(func):
    def wrapper():
        print("Going to say goodbye")
        func()
        print("see you tomorrow")
    return wrapper

@dec
def say_goodbye():
    print("Goodbye")

say_goodbye()
