# Recursion is when a function calls its self. You need to have a base case or an infinite loop can happen.
# The function will keep calling itself until the base case is reached. That then gets returned up the chain

# A classic example is to print the Fibonacci serries.
# For this fib if we go with n = 4 it will skip the first if and go to fib(2) + fib(3).
# These then call the function. fib(2) will pass the if and go to the else and call fib(0) + fib(1)
# Since fib(0) and fib(1) meet the base case they will return 0 and 1. This whole process will happen for fib(3) as well.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(4))
print(fibonacci(10))