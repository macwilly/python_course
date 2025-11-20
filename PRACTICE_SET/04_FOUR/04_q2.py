"""
Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
"""

# def sum_of_digits(n):

def sum_of_digits(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: add last digit to sum of remaining digits
    return n % 10 + sum_of_digits(n // 10)

# Example usage:
print(sum_of_digits(13))
