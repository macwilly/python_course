try:
    file_text = '''
    This is an example file.
    It has not one,
    But three lines of text.
    '''
    file_object = open("tasks.txt", "w")
    file_object.write(file_text)
    file_object.close()
except FileNotFoundError:
    print("File not found")