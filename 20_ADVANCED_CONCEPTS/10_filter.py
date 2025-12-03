# filter is a higher-order function that will operate on iterables. filter({function}, {iterable})
#  the function that is passed to filter should return True which will then add the iterable items a filter object that
#       is returned
# the function can be a standalone function or a lambda function

def is_even(x):
    ret = False
    if x % 2 == 0:
        ret = True
    return ret

number_list = [1,2,3,4,5,6]

is_even_list = filter(is_even, number_list)
print(list(is_even_list))

# With Lambda function

is_odd_list = filter(lambda x: x%2 != 0, number_list)
print(list(is_odd_list))