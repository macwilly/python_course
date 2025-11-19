"""
Write a function full_name(first, last) that takes first name and last name
as parameters and returns a single string in the format "First Last" .
"""

def full_name(first, last):
    """ Return a string of first and last name """
    return f"{first} {last}."

print(full_name("John", "Doe"))