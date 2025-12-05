
'''

def sum (a,b):
    return a+b
 print(sum(1,2, 7)) will get error
'''

def sum(*args):
    # args is a tuple of all the values passed
    print(args, type(args))
    total = 0
    for arg in args:
        total += arg
    return total

print(sum(1, 2, 7))
