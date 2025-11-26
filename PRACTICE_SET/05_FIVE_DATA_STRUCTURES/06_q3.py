def dict_merge(d1, d2):
    d1.update(d2)
    return d1


a1 = {"a": 1, "b": 2}
a2 = {"c": 3, "d": 4}

print(dict_merge(a1, a2))