import argparse
import os

def main():
    print(os.getcwd())
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="The name of the file")
    args = parser.parse_args()
    try:
        with open(args.filename) as f:
            number_of_lines = 0
            for line in f.readlines():
                number_of_lines += 1
            f.close()
            print(number_of_lines)
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()