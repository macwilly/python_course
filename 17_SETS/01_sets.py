# Sets are an unordered list of unique items
# The order in which the items are accessed is random (printed multiple times and it is not always the same as the
# way they were added
# They also do not have an index

fruit_set = {"apple", "banana", "orange"}
print(fruit_set)
fruit_set.add("apple") # This did not add anything
print(fruit_set)
fruit_set.add("grape")
print(fruit_set)

print(1)
set_string = str(fruit_set)
print(set_string)
print(2)
# Item needs to be in set or will get an error
fruit_set.remove("banana")
# Does a safe check to get rid of element. If it is not present no error will be thrown.
fruit_set.discard("banana")
print(fruit_set)
