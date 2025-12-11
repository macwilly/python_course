# open uses the file source and the mode. Modes can be combined such as 'rt' and 'rb'
"""
MODES
Character  Meaning
'r'        open for reading (default)
'w'        open for writing, truncating the file first
'x'        open for exclusive creation, failing if the file already exists
'a'        open for writing, appending to the end of file if it exists
'b'        binary mode
't'        text mode (default)
'+'        open for updating (reading and writing)
"""
try:
    file = open("../resources/mac.txt", "rt")
    content = file.read()
    print(content)
finally:
    file.close()

