"""
Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
their squares.
"""

list_1 = [1,2,3,4,5]

square_list = map(lambda num: num * num, list_1)
print(list(square_list))