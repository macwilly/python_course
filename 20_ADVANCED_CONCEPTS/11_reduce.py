# reduce is a higher-order function that will operate on iterables. reduce({function}, {iterable})
#  reduce will apply to two arguments in order from left to right until only a single value remains
# the function can be a standalone function or a lambda function

from functools import reduce

number = [1,2,3,4,5]

def sum(x,y):
    return x+y
# 1 + 2 + 3 + 4 + 5
# 3 + 3 + 4 + 5
# 6 + 4 + 5
# 10 + 5
# 15
print(reduce(sum, number))

product = reduce(lambda x,y: x*y, number)
print(product)
