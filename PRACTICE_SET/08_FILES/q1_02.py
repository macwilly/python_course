try:
    file_object = open("notes.txt", "r")
    file_contents = file_object.read()
    print(file_contents)
    file_object.close()
except FileNotFoundError:
    print("File not found")