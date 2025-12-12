try:
    file_object = open("tasks.txt", "a")
    file_object.write("\nTask Completed\n")
    file_object.close()
except FileNotFoundError:
    print("File not found")