try:
    file_object = open("notes.txt", "w")
    file_object.write("Learning Python is fun!")
    file_object.close()
except FileNotFoundError:
    print("File not found")