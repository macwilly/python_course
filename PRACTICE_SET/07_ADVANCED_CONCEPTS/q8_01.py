from functools import reduce
def sum_all(*args):
    return reduce(lambda x, y: x + y, args)
print(sum_all(1,2,3,4,5))