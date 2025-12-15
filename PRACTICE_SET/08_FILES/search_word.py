import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="The name of the file")
    parser.add_argument("word", type=str, help="The word to search")
    args = parser.parse_args()

    try:
        with open(args.filename, "r") as file_object:
            file_content = file_object.read()
            file_content = file_content.lower().split()
            search_word = args.word.lower()
            print(f"{search_word} was found {file_content.count(search_word)} time")
            file_object.close()
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()