from functools import reduce
import time


def timer(func):
    def wrapper():
        start_time = time.perf_counter_ns()
        func()
        end_time = time.perf_counter_ns()
        print(end_time - start_time)
    return wrapper


@timer
def sum_large_number():
    large_list = []
    for i in range(1, 1000001):
        large_list.append(i)
    return reduce(lambda x, y: x + y, large_list)


sum_large_number()
