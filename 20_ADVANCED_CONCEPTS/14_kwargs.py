def marks(**kwargs):
    # kwargs is a dict of all the values passed KEY WORD args
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

marks(jeff=5,steff=8,jim=7)