f = "../resources/mac.txt"
try:
    file_object = open(f, "r")
    for line in file_object:
        print(f"{line} has {len(line)} characters")

    file_object.close()
except FileNotFoundError:
    print("File not found")
