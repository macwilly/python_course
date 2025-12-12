import shutil

shutil.copy("./tasks.txt", "./my_folder/tasks.txt")
shutil.move("./notes.txt", "./my_folder/notes.txt")
shutil.rmtree("./my_folder")