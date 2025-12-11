from functools import wraps


def universal_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)
        print(f"result: {result}")
        return result
    return wrapper

@universal_decorator
def sub(a,b):
    return a - b

@universal_decorator
def hello(name, message="Hello World!"):
    return f"{name} says {message}"

print(hello(name="Mackenzie", message="Hello World!"))
print(sub(10,5))