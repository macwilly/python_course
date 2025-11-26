# This of set operations like SQL table operations
# UNION
# INTERSECT
set_a = {2,55,654,5}
set_b = {12,5,64}

c = set_a.union(set_b)
print(c)

d = set_a.symmetric_difference(set_b)
print(d)

e = set_a.intersection(set_b)
print(e)

# will return a set will the values of a that are not in b
f = set_a.difference(set_b)
print(f)