"""
Write a function calculate_area(length, width=10) that returns the area of
a rectangle. Test it by calling the function with:
 * Both length and with
 * Only length (use default width)
"""

def calculate_area(length, width=10):
    """ Return the area of a rectangle. Default width is 10. """
    return length * width

print(calculate_area(10))
print(calculate_area(10,11))
print(calculate_area(width=5,length=5))