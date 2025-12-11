ext = ".txt"
file_name = "test2"
file_path = "../resources/"
file = file_path + file_name + ext
file_object = open(file, "a")
string = "One Liner2"
# When appending a one line string it will not add any new line characters
file_object.write(string)
file_object.close()
