print("Hello World")
# print() function will take multiple arguments and add a space between them.
# print() function will by default add a new line to the end of the statement.
print("Hello World", "Mac")

"""
 Print function from Python Documentation
  print(*objects, sep=' ', end='\n', file=None, flush=False)
 print will take any number of objects to write 
 sep will determine what character to use when multiple object arguments are used
 end will determine what the end character of the print function will be
 file will write to a file but must be used with an object that has write(string)
 flush = False will allow python to buffer the output
 flush = True Python forces the output to be written immediately
"""

print("Hello","World", sep="_",end="!")
print("This is from another line")
