import os
current_working_directory = os.getcwd()
print(current_working_directory)

files_in_cwd = os.listdir(current_working_directory)
print(files_in_cwd)

os.mkdir(current_working_directory + "/my_folder")
