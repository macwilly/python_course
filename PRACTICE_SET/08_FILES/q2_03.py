try:
    file_object = open("tasks.txt", "r")
    for line in file_object.readlines():
        print(line)
except FileNotFoundError:
    print("File not found")