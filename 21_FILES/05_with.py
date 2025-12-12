file_object  = open("../resources/mac.txt", "r")
content = file_object.read()
print(content)
file_object.close()

# Using with is a shortened way to open and close a file object
# with is a context manager
try:
    with open("../resources/mac.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")
