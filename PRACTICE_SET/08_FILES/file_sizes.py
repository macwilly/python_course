import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument( "directory", type=str, help="The directory to search for files")
args = parser.parse_args()

try:
    os.path.isdir(args.directory)
    dir_list = os.listdir(args.directory)
    print(dir_list)
    total_size = 0
    for file in dir_list:
        file_path = os.path.join(args.directory, file)
        file_size = os.path.getsize(file_path)
        total_size += file_size
        print(f"{file} is {file_size} bytes")

    print(f"Total size of {args.directory} is {total_size} bytes")
except IsADirectoryError:
    print("Directory is not a file")