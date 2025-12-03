# Map is a higher-order function that will operate on iterables. map({function}, {iterable})
# the map will run the function on each of the items in the iterable and then return a map object
# the function can be a standalone function or a lambda function

numbers_list = [1,2,3,4,5]

def square(x):
    return x * x

mapped = map(square, numbers_list)
# remember mapped is a map object. As such it will print its object location in memory so it will need to be type cast
print(list(mapped))

# Same thing but with lambda function

numbers_list_two = [1,2,3,4,5]

mapped_two = map(lambda x: x*x, numbers_list_two)

print(list(mapped_two))