# Think about alot of the os commands like linux or power shell commands.
# os.rmdir will only remove an empty directory
import os

a = os.listdir("../resources")
current_working_directory  = os.getcwd()
print(a)
print(current_working_directory) #pwd

# to delete a file will use this will not remove a directory
#os.remove("")