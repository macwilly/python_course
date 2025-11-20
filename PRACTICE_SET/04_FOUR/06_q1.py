"""
Write a function increment() that has a local variable counter initialized to
0 and increments it by 1 each time it is called. Observe whether the value
persists across function calls.
"""

def increment():
    counter = 0
    counter += 1
    return counter

increment()
print(increment())
# Will never go above 1