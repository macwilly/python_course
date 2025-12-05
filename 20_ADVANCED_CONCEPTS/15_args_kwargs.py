"""
You need to do args first then kwargs
"""
def func1(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


func1(1,2,3,4, conn=True,dis=None)
