import os

tempfile = open("1.tmp", "w")
tempfile.close()

file_list = os.listdir(".")
print(file_list)
for file in file_list:
    if file.endswith(".tmp"):
        os.remove(file)
file_list = os.listdir(".")
print(file_list)