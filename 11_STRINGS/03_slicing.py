# Slice Syntax Recap string[start:stop:step]
# In Slicing the first argument is the index to start at. the second argument is the index -1 to stop at
# the default of the first argument is 0
# With a -1 as the second argument it will return from the given start index to the end of the string.
# Doing ::-1 will print the whole string in reverse
name = "MackenzieWillard"

print(name[3:5])
print(name[3:-1])
print(name[::-1])

# Step the step works off of n -1
print(name[::2])