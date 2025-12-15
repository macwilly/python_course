try:
    with (open("testfile.txt", "r") as f):
        file_contents = f.read()
        file_contents = file_contents.upper()
        f.close()
        upper_file = open("testfiletwo.txt", "w")
        upper_file.write(file_contents)
        upper_file.close()
except FileNotFoundError:
    print("File not found")