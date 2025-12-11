ext = ".txt"
file_name = "test"
file_path = "../resources/"

file = file_path + file_name + ext
string = '''
 Hello World!
 This is a new file with
 multi-line
'''
# Just writing the file will create a new file every time.
file_object = open(file, "w")
file_object.write(string)
file_object.close()

