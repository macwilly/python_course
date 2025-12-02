def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator


@repeat(3) #this is calling the outer layer of repeat
def hello(name): # since the wrapper is taking an argument we need to ensure our function takes and argument as well
    print('hello' + name)

hello("Tiger")

# can also redefine the function without the decorator
def hello():
    print('hi')

hello()