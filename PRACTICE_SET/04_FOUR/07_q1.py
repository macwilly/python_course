"""
Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.

0 1 2 3 4 5
0 1 1 2 3 5
"""

# by setting the a and be to defaults still allows for fibonacci(n). This does do less calculation but could cause user error
def fibonacci(n, a=0, b=1):
    # Base case: if n is 0, stop
    if n <= 0:
        return
    # Print current number
    print(a, end=" ")
    # Recursive call with next pair
    fibonacci(n - 1, b, a + b)

# Example usage:
fibonacci(10)




def fibonacci_2(n):
    '''
    Print the first n Fibonacci numbers using recursion.
    '''
    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    for i in range(n):
        print(fib(i), end=" ")

# Example usage
fibonacci_2(10)   # Prints: 0 1 1 2 3 5 8 13 21 34
